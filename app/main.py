import os
import subprocess

def check_directory_exists(directory) -> bool:
    """Проверяет, существует ли указанная директория."""
    if not os.path.exists(directory):
        print(f"Ошибка: Директория {directory} не существует.")
        return False
    return True

def create_directory(directory):
    """Создает директорию, если она не существует."""
    os.makedirs(directory, exist_ok=True)

def get_png_files(input_dir):
    """Возвращает список всех PNG файлов в указанной директории."""
    return [f for f in os.listdir(input_dir) if f.endswith('.png')]

def convert_file(input_path, output_path):
    """Конвертирует один PNG файл в SVG с помощью convert и potrace."""
    ppm_file = input_path.replace('.png', '.ppm')

    try:
        # Используем convert для преобразования PNG в PPM
        subprocess.run(["convert", input_path, ppm_file], check=True)
        print(f"Успешно конвертирован PNG в PPM: {input_path} -> {ppm_file}")

        # Используем potrace для преобразования PPM в SVG
        subprocess.run(["potrace", ppm_file, "-s", "-o", output_path], check=True)
        print(f"Успешно конвертирован PPM в SVG: {ppm_file} -> {output_path}")

        # Удаляем временный PPM файл
        os.remove(ppm_file)

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при конвертации {input_path}: {e}")

def convert_png_to_svg(input_dir, output_dir):
    """Основная функция для конвертации всех PNG файлов в директории в SVG."""
    if not check_directory_exists(input_dir):
        return

    create_directory(output_dir)

    files = get_png_files(input_dir)

    if not files:
        print("В папке с PNG-файлами нет файлов для конвертации.")
        return

    for file in files:
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file.replace('.png', '.svg'))
        convert_file(input_path, output_path)

if __name__ == "__main__":
    workspace_dir = "/app/workspace"
    png_dir = os.path.join(workspace_dir, "pngs")
    svg_dir = os.path.join(workspace_dir, "outputssvg")

    convert_png_to_svg(png_dir, svg_dir)
