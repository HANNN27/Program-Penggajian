# PROGRAM PENGGAJIAN KARYAWAN
import os
import sys
import time

tanggal = time.strftime("%d-%m-%y %H:%M:%S")

def move(label) :
    global number
    number = label

def clearscreen() :
    os.system('cls')

def exit() :
    sys.exit()

def gol_A() :
    upah_perjam = 75000
    gaji = upah_perjam * jamKerja
    bpjs_kerja = 100000
    bpjs_kesehatan = 85000
    pph = gaji * 0.02
    gajiBersih = gaji - bpjs_kesehatan - bpjs_kerja - pph
    print(f'Gaji Pokok  : Rp.{gaji}')
    print(f'Biaya Pph   : Rp.{pph}')
    print(f'BPJS K/k    : Rp.{bpjs_kerja}')
    print(f'BPJS Kes    : Rp.{bpjs_kesehatan}')
    print('-'*30)
    print(f'Gaji Bersih : Rp.{gajiBersih}')
    print(f'Tanggal     : {tanggal}')

def gol_B() :
    upah_perjam = 60000
    gaji = upah_perjam * jamKerja
    bpjs_kerja = 100000
    bpjs_kesehatan = 85000
    pph = gaji * 0.02
    gajiBersih = gaji - bpjs_kesehatan - bpjs_kerja - pph
    print(f'Gaji Pokok  : Rp.{gaji}')
    print(f'Biaya Pph   : Rp.{pph}')
    print(f'BPJS K/k    : Rp.{bpjs_kerja}')
    print(f'BPJS Kes    : Rp.{bpjs_kesehatan}')
    print('-'*31)
    print(f'Gaji Bersih : Rp.{gajiBersih}')
    print(f'Tanggal     : {tanggal}')

def gol_C() :
    upah_perjam = 40000
    gaji = upah_perjam * jamKerja
    bpjs_kerja = 100000
    bpjs_kesehatan = 85000
    pph = gaji * 0.02
    gajiBersih = gaji - bpjs_kesehatan - bpjs_kerja - pph
    print(f'Gaji Pokok  : Rp.{gaji}')
    print(f'Biaya Pph   : Rp.{pph}')
    print(f'BPJS K/k    : Rp.{bpjs_kerja}')
    print(f'BPJS Kes    : Rp.{bpjs_kesehatan}')
    print('-'*31)
    print(f'Gaji Bersih : Rp.{gajiBersih}')
    print(f'Tanggal     : {tanggal}')

def gol_D() :
    upah_perjam = 25000
    gaji = upah_perjam * jamKerja
    bpjs_kerja = 100000
    bpjs_kesehatan = 85000
    pph = gaji * 0.02
    gajiBersih = gaji - bpjs_kesehatan - bpjs_kerja - pph
    print(f'Gaji Pokok  : Rp.{gaji}')
    print(f'Biaya Pph   : Rp.{pph}')
    print(f'BPJS K/k    : Rp.{bpjs_kerja}')
    print(f'BPJS Kes    : Rp.{bpjs_kesehatan}')
    print('-'*31)
    print(f'Gaji Bersih : Rp.{gajiBersih}')
    print(f'Tanggal     : {tanggal}')

def cetak() :
    print('='*8 + ' PT.SUN FLOWER ' + '='*8)
    print(f'Nama        : {name}')
    print(f'Golongan    : {gol}')
    print(f'Kerja       : {hariKerja} Hari / {jamKerja} Jam')
    print('='*31)

def repeat() :
    repeat = input('\nIngin lanjut ? [y/n] : ')
    if repeat == 'y' or repeat == 'Y':
        move(0)
        clearscreen()
    elif repeat == 'n' or repeat == 'N' :
        clearscreen()
        exit()
    else :
        exit()

while True :
    print("""
    =====================================
    |                                   |
    |       PROGRAM HITUNG GAJI         |
    |       KELOMPOK SUN FLOWER         |
    |                                   |
    =====================================""")
    print('\n\tSILAHKAN UNTUK MENGISI DATA')
    name = str(input('\n\tNama : '))
    gol = str(input('\tGolongan [A/B/C/D] : '))
    hariKerja = int(input('\tHari Kerja Dalam Sebulan : '))
    jamKerja = hariKerja * 8
    clearscreen()
    if gol == 'a' or gol == 'A' :
        cetak()
        gol_A()
    elif gol == 'b' or gol == 'B' :
        cetak()
        gol_B()
    elif gol == 'c' or gol == 'C' :
        cetak()
        gol_C()
    elif gol == 'd' or gol == ' D' :
        cetak()
        gol_D()
    else :
        exit()
    repeat()