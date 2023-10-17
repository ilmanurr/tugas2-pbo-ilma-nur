#include <iostream>
#include <cmath>
using namespace std;

class BangunDatar {
    public :
        virtual void inputData() = 0;
        virtual void hitungLuas() = 0;
        virtual void hitungKeliling() = 0;
};

class Persegi : public BangunDatar {
    private : 
        double sisi;

    public : 
        void inputData() override {
            cout << "Masukkan panjang sisi persegi : ";
            cin >> sisi;
        }

        void hitungLuas() override {
            cout << "Luas persegi : " << sisi * sisi << endl;
        }

        void hitungKeliling() override {
            cout << "Keliling persegi : " << 4 * sisi << endl;
        }
};

class PersegiPanjang : public BangunDatar {
    private :
        double panjang;
        double lebar;

    public :
        void inputData() override {
            cout << "Masukkan panjang persegi panjang : ";
            cin >> panjang;
            cout << "Masukkan lebar persegi panjang : ";
            cin >> lebar;
        }

        void hitungLuas() override {
            cout << "Luas persegi panjang : " << panjang * lebar << endl;
        }

        void hitungKeliling() override {
            cout << "Keliling pesegi panjang : " << 2 * (panjang + lebar) << endl;
        }
};

class Segitiga : public BangunDatar {
    private :
        double sisi1;
        double sisi2;
        double sisi3;
        double alas;
        double tinggi;

    public :
        void inputData() override {
            cout << "Masukkan panjang sisi 1 segitiga : ";
            cin >> sisi1;
            cout << "Masukkan panjang sisi 2 segitiga : ";
            cin >> sisi2;
            cout << "Masukkan panjang sisi 3 segitiga : ";
            cin >> sisi3;
            cout << "Masukkan panjang alas segitiga : ";
            cin >> alas;
            cout << "Masukkan tinggi segitiga : ";
            cin >> tinggi;
        }

        void hitungLuas() override {
            cout << "Luas segitiga : " << 0.5 * alas * tinggi << endl;
        }

        void hitungKeliling() override {
            cout << "Keliling segitiga : " << sisi1 + sisi2 + sisi3 << endl;
        }
};

class Lingkaran : public BangunDatar {
    private :
        double jarijari;
    
    public :
        void inputData() override {
            cout << "Masukkan jari-jari lingkaran : ";
            cin >> jarijari;
        }

        void hitungLuas() override {
            cout << "Luas lingkaran : " << 3.14 * jarijari * jarijari << endl;
        }

        void hitungKeliling() override {
            cout << "Keliling lingkaran : " << 2 * 3.14 * jarijari << endl;
        }
};

int main() {
    int pilihan;
    BangunDatar* bangunDatar;

    do {
        cout << "\n----------------------KALKULATOR BANGUN DATAR----------------------\n";
        cout << "Pilihan jenis bangun datar : " << endl;
        cout << "1. Persegi" << endl;
        cout << "2. Persegi Panjang" << endl;
        cout << "3. Segitiga" << endl;
        cout << "4. Lingkaran" << endl;
        cout << "0. Keluar" << endl;
        cout << "Masukkan pilihan Anda : ";
        cin >> pilihan;
        cout << endl;

        switch (pilihan)
        {
        case 1 :
            bangunDatar = new Persegi();
            break;
        case 2 :
            bangunDatar = new PersegiPanjang();
            break;
        case 3 :
            bangunDatar = new Segitiga();
            break;
        case 4 :
            bangunDatar = new Lingkaran();
            break;
        case 0 :
            cout << "Program selesai!" << endl;
            return 0;
        
        default:
            cout << "Pilihan yang Anda masukkan tidak valid! Silahkan coba lagi." << endl;
            break;
        }

        bangunDatar->inputData();
        bangunDatar->hitungLuas();
        bangunDatar->hitungKeliling();

        delete bangunDatar;
    } while (pilihan != 0);

    return 0;
}