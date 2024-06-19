# Solicitar al usuario el nombre del archivo a buscar
$archivoABuscar = Read-Host "Introduce el nombre (o parte del nombre) del archivo que deseas buscar"

# Directorio donde iniciar la búsqueda (puedes cambiarlo según tu necesidad)
$directorioInicial = "\\fserver\Finanzas"

# Buscar el archivo filtrando por nombre
$resultados = Get-ChildItem -Path $directorioInicial -Recurse | Where-Object { $_.Name -like "*$archivoABuscar*" }

# Mostrar los resultados
if ($resultados) {
    Write-Host "Se encontraron los siguientes archivos con el nombre '$archivoABuscar':"
    $resultados | ForEach-Object {
        Write-Host $_.FullName
    }
    
    # Mantener la ventana abierta durante 10 minutos
    Start-Sleep -Seconds 600
} else {
    Write-Host "No se encontraron archivos con el nombre '$archivoABuscar' en $directorioInicial"
    
    # Mantener la ventana abierta durante 10 minutos
    Start-Sleep -Seconds 600
}
