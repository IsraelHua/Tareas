#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <limits>
using namespace std;

struct Registro {
    string fecha;
    double venta;
};

int main() {
    ifstream archivoEntrada("ventas_diarias.txt");
    ofstream archivoSalida("resumen_ventas.txt");
    
    if (!archivoEntrada.is_open()) {
        cerr << "No se pudo abrir el archivo de entrada." << endl;
        return 1;
    }
    
    if (!archivoSalida.is_open()) {
        cerr << "No se pudo abrir el archivo de salida." << endl;
        return 1;
    }
    
    string linea;
    Registro maxVenta, minVenta;
    maxVenta.venta = -numeric_limits<double>::infinity();  // Inicializa a un valor muy bajo
    minVenta.venta = numeric_limits<double>::infinity();   // Inicializa a un valor muy alto
    double ventaTotal = 0.0;
    int contador = 0;
    
    while (getline(archivoEntrada, linea)) {
        stringstream ss(linea);
        Registro registro;
        if (getline(ss, registro.fecha, ',') && ss >> registro.venta) {
            ventaTotal += registro.venta;
            contador++;
            
            if (registro.venta > maxVenta.venta) {
                maxVenta = registro;
            }
            if (registro.venta < minVenta.venta) {
                minVenta = registro;
            }
        } else {
            cerr << "Error: formato incorrecto en la línea: " << linea << endl;
        }
    }
    
    archivoEntrada.close();
    
    double promedioVentas = (contador > 0) ? (ventaTotal / contador) : 0.0;
    
    archivoSalida << "Venta total: " << ventaTotal << endl;
    archivoSalida << "Promedio de ventas: " << promedioVentas << endl;
    archivoSalida << "Día de mayor venta: " << maxVenta.fecha << ", " << maxVenta.venta << endl;
    archivoSalida << "Día de menor venta: " << minVenta.fecha << ", " << minVenta.venta << endl;
    
    archivoSalida.close();
    
    cout << "Procesamiento completo. Resultados guardados en 'resumen_ventas.txt'." << endl;
    
    return 0;
}

