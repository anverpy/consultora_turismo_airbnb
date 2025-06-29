#!/usr/bin/env python3
# Script para eliminar columnas específicas de listings_nuevo.csv

import pandas as pd
import os

print('🔄 Eliminando columnas avg_price_summer y price_weekend de listings_nuevo.csv')
print('=' * 70)

# Cargar el dataset
try:
    df = pd.read_csv('listings_nuevo.csv')
    print(f'📂 Dataset cargado exitosamente')
    print(f'📊 Shape original: {df.shape}')
    print(f'📋 Columnas originales: {len(df.columns)}')
    
    # Mostrar las columnas que vamos a eliminar
    columns_to_drop = ['avg_price_summer', 'price_weekend']
    print(f'\n🗑️  Columnas a eliminar: {columns_to_drop}')
    
    # Verificar que existen
    existing_cols = [col for col in columns_to_drop if col in df.columns]
    missing_cols = [col for col in columns_to_drop if col not in df.columns]
    
    if existing_cols:
        print(f'✅ Columnas encontradas: {existing_cols}')
    if missing_cols:
        print(f'❌ Columnas no encontradas: {missing_cols}')
    
    # Eliminar las columnas que existen
    if existing_cols:
        df_cleaned = df.drop(columns=existing_cols)
        print(f'\n📊 Shape después de eliminar: {df_cleaned.shape}')
        print(f'📋 Columnas restantes: {len(df_cleaned.columns)}')
        
        # Guardar el archivo actualizado
        df_cleaned.to_csv('listings_nuevo.csv', index=False)
        print(f'\n✅ Archivo listings_nuevo.csv actualizado y guardado')
        print(f'🎉 Operación completada exitosamente')
        
        # Verificar el resultado
        print(f'\n🔍 Verificación final:')
        df_verification = pd.read_csv('listings_nuevo.csv')
        print(f'📊 Shape final: {df_verification.shape}')
        print(f'📋 Columnas finales: {list(df_verification.columns)}')
        
    else:
        print(f'\n⚠️  No se encontraron columnas para eliminar')

except Exception as e:
    print(f'❌ Error: {e}')
