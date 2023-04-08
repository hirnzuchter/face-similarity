#Add this to the model collection in model.ipynb

def reduction_alt(self):
    self.add(Conv2D(1, (img_dim//2, img_dim//2), use_bias=False))
    self.add(Decouple(img_dim//2+1))
    self.add(Conv2D(1, (img_dim//4, img_dim//4), use_bias=False))
    self.add(Decouple(img_dim//4+2))
    self.add(Conv2D(10, (img_dim//8, img_dim//8), use_bias=False))
    self.add(Decouple(img_dim//8+3))
    self.add(Conv2D(10, (img_dim//8, img_dim//8), use_bias=False))
    self.add(Decouple(4))
    self.add(Conv2D(1, (4, 4), use_bias=False))
    self.add(Decouple(1))
    self.add(Flatten())
    self.add(Dense(8, use_bias=False))
    self.add(Dropout(0.1))
    self.add(Dense(4, use_bias=False))
    self.add(Dense(2, use_bias=False))
    self.add(Dense(1, activation=sigmoid, bias_constraint=unitnorm()))