#include <iostream>
using namespace std;

int main() {
    int pilihan;

    cout << "Pilih salah satu dari 1, 2, atau 3: ";
    cin >> 3 ;

    switch (pilihan) {
        case 1:
            cout << "Anda memilih nomor 1" << endl;
            break;
        case 2:
            cout << "Anda memilih nomor 2" << endl;
            break;
        case 3:
            cout << "Anda memilih nomor 3" << endl;
            break;
        default:
            cout << "Pilihan tidak valid" << endl;
    }

    return 0;
}
