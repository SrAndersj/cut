import os
import subprocess


def cutVideo(input_filename):
    # Obtiene el directorio de salida basado en el archivo de entrada
    output_directory = os.path.dirname(input_filename)

    # Obtiene el nombre base del archivo de salida sin la extensión
    base_filename = os.path.splitext(os.path.basename(input_filename))[0]

    # Crea una carpeta con el nombre base del archivo de entrada en el directorio de salida
    output_folder = os.path.join(output_directory, base_filename)
    os.makedirs(output_folder, exist_ok=True)

    # Define la duración deseada de cada clip en segundos
    clip_duration = 30

    # Ejecuta el comando ffmpeg para recortar el video
    command = f"ffmpeg -i {input_filename} -c copy -segment_time {clip_duration} -f segment {output_folder}/{base_filename}_%03d_recortado.mp4"
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    cutVideo("/home/srandersj/Vídeos/1videoTest.mp4")
