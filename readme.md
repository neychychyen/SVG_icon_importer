<h2 align = 'center'>Импорт изображений в svg</h2>

<details>
    <summary>О приложении</summary>
	<p>Импортирует все изображения в формате .png из папки /data/pngs в формате svg, используя POtrace Через docker-контейнер</p>
</details>

<details>
<summary>Установка</summary>
<p>Для приложения должен быть обязательно установлен <a href="https://www.docker.com/products/docker-desktop/">docker desktop</a></p>     
<hr>
Инструкция по запуску
1. Командной строкой склонируйте репозиторий:
    ```bash
    git clone https://github.com/neychychyen/SVG_icon_importer.git
    ```
2. Очистите `./data/pngs/`.
3. Поместите изображения в папку `./data/pngs/`.
4. Запустите docker-контейнер в командной строке в папке с проектом командой:
    ```bash
    docker-compose up -d --build
    ```
5. SVG-элементы хранятся в `./data/outputsvgs`.

</details>



