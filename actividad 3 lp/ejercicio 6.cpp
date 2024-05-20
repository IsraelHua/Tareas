#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <map>

int main() {
    std::ifstream inputFile("log.txt");
    std::ofstream outputFile("summary.txt");

    if (!inputFile.is_open()) {
        std::cerr << "Error al abrir el archivo de entrada." << std::endl;
        return 1;
    }

    if (!outputFile.is_open()) {
        std::cerr << "Error al abrir el archivo de salida." << std::endl;
        return 1;
    }

    std::map<std::string, int> errorCount;
    std::regex errorRegex("ERROR (\\d{3}):");

    std::string line;
    while (std::getline(inputFile, line)) {
        std::smatch match;
        if (std::regex_search(line, match, errorRegex)) {
            // La expresi�n regular encontr� un c�digo de error
            if (match.size() > 1) {
                // El c�digo de error se encuentra en el segundo grupo capturado por la expresi�n regular
                std::string errorCode = match.str(1);
                // Incrementa el contador para este c�digo de error
                errorCount[errorCode]++;
            }
        }
    }

    inputFile.close();

    // Escribir el resumen en el archivo de salida
    for (const auto& entry : errorCount) {
        outputFile << "ERROR " << entry.first << ": " << entry.second << std::endl;
    }

    outputFile.close();

    return 0;
}



