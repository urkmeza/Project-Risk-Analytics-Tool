import pandas as pd
import numpy as np

def calculate_pert_and_risk(planned, optimistic, pessimistic, risk_factor, complexity):
    """
    PMP metodolojisindeki PERT analizini ve özel risk skorlamasını uygular.
    """
    # PERT Formülü: (O + 4P + Pes) / 6
    expected_duration = (optimistic + (4 * planned) + pessimistic) / 6
    
    # Risk Skoru: Süre sapması ile paydaş karmaşıklığı ve dış risklerin kombinasyonu
    [cite_start]#  30+ paydaş yönetimi tecrübesine dayanarak kurgulanmıştır.
    base_risk = expected_duration / planned
    weighted_risk = base_risk * (1 + (risk_factor * (complexity / 5)))
    
    return round(weighted_risk, 2)

# [cite_start]Örnek Proje Verileri (Mısır Projesi gibi büyük çaplı işlerden esinlenilmiştir [cite: 14])
data = {
    'TaskName': ['Üretim Hattı Transferi', 'Vendor Seçimi', 'Ekipman Kurulumu', 'ISO Denetim Hazırlığı'],
    'PlannedDays': [45, 20, 30, 15],
    'OptimisticDays': [40, 15, 25, 12],
    'PessimisticDays': [70, 40, 50, 25],
    [cite_start]'RiskFactor': [0.6, 0.4, 0.3, 0.2], #  Vendor ve kurulum riskleri
    [cite_start]'Complexity': [5, 4, 3, 2] # [cite: 15] Paydaş karmaşıklık seviyesi
}

df = pd.DataFrame(data)

# Risk analizini uygula
df['Risk_Score'] = df.apply(lambda x: calculate_pert_and_risk(
    x['PlannedDays'], x['OptimisticDays'], x['PessimisticDays'], 
    x['RiskFactor'], x['Complexity']), axis=1)

# Kritiklik seviyesini belirle
df['Status'] = np.where(df['Risk_Score'] > 1.3, 'CRITICAL', 'STABLE')

print("--- Proje Risk Analiz Raporu ---")
print(df[['TaskName', 'Risk_Score', 'Status']].sort_values(by='Risk_Score', ascending=False))
