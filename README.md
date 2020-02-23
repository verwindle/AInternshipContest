Ссылка на скачивание данных: [link](https://www.immersivelimit.com/datasets/cigarette-butts).

Данные представляют из себя набор синтетически сгенерированных фотографий окурков сигарет и маски, определяющей их на фотографии, а также координаты ограничивающего их бокса.

Доступные данные разделены на несколько папок:  
- `real_test` содержит фотографии 512x512x3;  
- `train/images` содержит фотографии 512x512x3;  
- `train/coco_annotations.json` содержит аннотации в формате [COCO](http://cocodataset.org/#format-data);  
- `val/images` содержит фотографии 512x512x3;  
- `val/coco_annotations.json` содержит аннотации в формате [COCO](http://cocodataset.org/#format-data).

Для запуска необходимо будет еще склонировать mask rcnn
git clone https://github.com/noelcodes/Mask_RCNN.git, сделать билд, добавить в папку logs.

Ссылка на логи - https://drive.google.com/drive/u/1/folders/1-Mqlblr0oO5HLXbb4H0ulJGegpVpug1i
