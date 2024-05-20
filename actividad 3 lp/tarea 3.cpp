#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>

int main() {
    std::ifstream inputFile("precios.txt");  
    std::ofstream outputFile("precios_soles.txt"); 

    const double tasa_conversion = 3.85; 

    std::string line;
    while (std::getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string producto;
        double precio_dolares;
        char delim; 
        std::getline(iss, producto, ',');
        iss >> precio_dolares >> delim;
        double precio_soles = precio_dolares * tasa_conversion;
        outputFile << std::fixed << std::setprecision(2) << producto << ", " << precio_soles << std::endl;
    }

    inputFile.close();
    outputFile.close();

    std::cout << "Los precios han sido convertidos y guardados en 'precios_soles.txt'." << std::endl;

    return 0;
}
