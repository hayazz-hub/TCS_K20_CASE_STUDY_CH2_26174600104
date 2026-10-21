# 15. Du doan ket qua truoc khi chay
# Du doan: dien_nang_kwh = 0.375, chi_phi = 1125.0

# Khai bao bien ban dau
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tinh dien nang tieu thu va chi phi dien
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In ca gia tri va kieu du lieu cua hai ket qua
print("Dien nang:", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi:", chi_phi, type(chi_phi))

# 16. Thay so_phut bang 60 roi chay lai va so sanh
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Dien nang moi (so_phut = 60):", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phi moi (so_phut = 60):", chi_phi, type(chi_phi))
