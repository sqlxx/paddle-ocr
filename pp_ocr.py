from paddleocr import PaddleOCR, draw_ocr
from PIL import Image, ImageDraw, ImageFont

ocr = PaddleOCR(use_angle_cls=True, lang="ch")
img_path = './imgs/fapiao.jpg'

result = ocr.ocr(img_path, cls=True)

image = Image.open(img_path).convert('RGB')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("./fonts/simfang.ttf", size=20)

for idx in range(len(result)):
  res = result[idx]
  for line in res:
    print(line[1])
    box = line[0]
    box = [(min(point[0] for point in box), min(point[1] for point in box)),
           (max(point[0] for point in box), max(point[1] for point in box))]
    txt = line[1][0]
    draw.rectangle(box, outline="red", width=2)

    draw.text((box[0][0], box[0][1] - 25), txt, fill="blue", font=font)
  
image.save("result.jpg")

# im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
# im_show = draw_ocr(image, boxes)
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')

