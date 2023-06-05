

def cutVideo(input_filename):



    import subprocess

    # Define el nombre del archivo de entrada y el nombre base del archivo de salida

    output_directory = "/home/srandersj/Vídeos/"
    output_filename_base = output_directory + "recortado"

    # Define la duración deseada de cada clip en segundos
    clip_duration = 30

    command = f"ffmpeg -i {input_filename} -c copy -segment_time {clip_duration} -f segment {output_filename_base}%03d.mp4"
    subprocess.call(command, shell=True)

    # Comando base de ffmpeg para recortar el video
    # -i <archivo_de_entrada>: Especifica el archivo de video de entrada
    # -c copy: Copia el flujo de video y audio sin realizar ninguna conversión
    # -segment_time <duración>: Establece la duración deseada de cada segmento o clip
    # -f segment: Indica el formato de salida de los segmentos
    # {output_filename_base}%03d.mp4: Nombre base para los archivos de salida, seguido de números secuenciales de tres dígitos para nombrar los archivos


if __name__ == '__main__':
    cutVideo("/home/srandersj/Vídeos/1videoTest.mp4")


