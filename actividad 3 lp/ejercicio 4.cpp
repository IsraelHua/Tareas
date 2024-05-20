#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>
using namespace std;

struct Registro {
    string fecha;
    double temperatura;
};

int main() {
    ifstream archivoEntrada("temperaturas.txt");
    ofstream archivoSalida("temperaturas_extremas.txt");
    
    if (!archivoEntrada.is_open()) {
        cerr << "No se pudo abrir el archivo de entrada." << endl;
        return 1;
    }
    
    if (!archivoSalida.is_open()) {
        cerr << "No se pudo abrir el archivo de salida." << endl;
        return 1;
    }
    
    string linea;
    Registro maxTemp, minTemp;
    maxTemp.temperatura = -numeric_limits<double>::infinity();  // Inicializa a un valor muy bajo
    minTemp.temperatura = numeric_limits<double>::infinity();   // Inicializa a un valor muy alto
    
    while (getline(archivoEntrada, linea)) {
        stringstream ss(linea);
        Registro registro;
        if (getline(ss, registro.fecha, ',') && ss >> registro.temperatura) {
            if (registro.temperatura > maxTemp.temperatura) {
                maxTemp = registro;
            }
            if (registro.temperatura < minTemp.temperatura) {
                minTemp = registro;
            }
        } else {
            cerr << "Error: formato incorrecto en la línea: " << linea << endl;
        }
    }
    
    archivoEntrada.close();
    
    archivoSalida << "Día de temperatura máxima: " << maxTemp.fecha << ", " << maxTemp.temperatura << endl;
    archivoSalida << "Día de temperatura mínima: " << minTemp.fecha << ", " << minTemp.temperatura << endl;
    
    archivoSalida.close();
    
    cout << "Procesamiento completo. Resultados guardados en 'temperaturas_extremas.txt'." << endl;
    
    return 0;
}



