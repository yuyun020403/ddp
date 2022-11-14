#----input data mahasiswa-----#
nim = input('Masukkan NIM:')
nama = str(input('Nama Anda:'))
nilai = float(input('Nilai Anda'))


#-----Print data nilai Mahasiswa----#
print("NIM \t\t: %s"
      "\nNama \t\t: %s"
      "\nNilai \t\t: %.2f" %(nim,nama,nilai)
      )


#-----tuple dan list lulus minimal 60,jika<=60 dinyatakan gagal----#
ket = ('Gagal','Lulus',) [nilai >= 60]
if nilai >= 85 and nilai < 100:
      grade = 'A'
      predikat = 'Memuaskan'
elif nilai >= 75 and nilai < 80:
      grade = 'B'
      predikat = 'Bagus'
elif nilai >= 60 and nilai < 75:
      grade = 'C'
      predikat = 'Cukup'
elif nilai >= 30 and nilai < 60:
      grade = 'D'
      predikat = 'Kurang'
else:
      grade = 'E'
      predikat = 'Buruk'


#---- output print----#
print('Keterangan: %s'
      '\nGrade\t: %s'
      '\nPredikat\t: %s'
      '\n------------------'
      % (ket,grade,predikat)
)

