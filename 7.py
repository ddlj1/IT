import cv2
import segmentation_models_pytorch as smp
import matplotlib.pyplot as plt
import torch

model=smp.Unet(
    encoder_name="resnet34",
    encoder_weights="imagenet",
    in_channesls=3,
    classes=1
)
model.eval()

img=cv2.imread("wall.png")
img=cv2.resize(img,(128,128))
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_tensor=torch.from_numpy(img).float().permute(2,0,1).unsqueeze(0)/2550

with torch.no_grad():
    mask=model(img_tensor)
    mask=torch.sigmoid(mask)
    mask_np=mask[0,0].numpy()

plt.subplot(1,2,1)
plt.title("imput image")
plt.imshow(img)

plt.subplot(1,2,2)
plt.title("predicted mask")
plt.imshow(mask_np,cmap="gray")

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
