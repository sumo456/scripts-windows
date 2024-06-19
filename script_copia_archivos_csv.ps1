# Definir el directorio a escanear
$directoryPath = "\\fserver\Finanzas\PGlobal"

# Obtener todos los archivos del directorio y subdirectorios
$files = Get-ChildItem -Path $directoryPath -Recurse | Where-Object { -not $_.PSIsContainer }

# Crear un objeto hash para almacenar los archivos por su hash
$fileHashTable = @{}

# Calcular el hash de cada archivo y almacenar en el hash table
foreach ($file in $files) {
    try {
        $hash = Get-FileHash -Path $file.FullName -Algorithm SHA256
        if ($fileHashTable.ContainsKey($hash.Hash)) {
            $fileHashTable[$hash.Hash] += ,$file.FullName
        } else {
            $fileHashTable[$hash.Hash] = @($file.FullName)
        }
    } catch {
        Write-Host "No se pudo calcular el hash del archivo: $($file.FullName)"
    }
}

# Crear una lista de objetos personalizados para exportar a CSV
$duplicateFiles = @()
foreach ($hash in $fileHashTable.Keys) {
    if ($fileHashTable[$hash].Count -gt 1) {
        foreach ($filePath in $fileHashTable[$hash]) {
            $duplicateFiles += [PSCustomObject]@{
                Hash = $hash
                FilePath = $filePath
            }
        }
    }
}

# Guardar el resultado en un archivo CSV
$outputPath = "C:\Users\dsalvador\OneDrive - PLIMON GLOBAL , SLU\Documentos\duplicados.csv"
$duplicateFiles | Export-Csv -Path $outputPath -NoTypeInformation

Write-Host "El análisis de duplicados ha finalizado. El resultado se ha guardado en $outputPath"
