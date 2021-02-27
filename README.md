# elfplott: Electric Field Plotting and Lorentz Transformation Tool
**El**ectric **F**ield **P**lotting and **Lo**rentz **T**ransformation **T**ool
Stego is a steganography software that allows the user to encode/decode a secret message within an album of PNG images.

## How to use

### Encode ASCII message string
1. Place PNGs inside `pool/`. 14 sample images are provided. 

2. To find maximum message length possible for given PNGs and `SPACING` parameter (see **Encoding method** for a description of this parameter), run from stego root: `python3 stego.py maxlen`

3. Run from stego root: `python3 stego.py e "secret message here"`. Processed images are stored in `encoded/`. (Images already in `encoded/` are deleted. Original images in `pool/` are unchanged.)


### Decode message
1. Ensure `encoded/` contains PNGs processed with Stego, and that `SPACING` defined in `stego.py` is the same as the one used to encode. 

2. Run from stego root: `python3 stego.py d`

## Encoding method
The goal of steganography is to avoid detection. Images are a perfect medium for this- in today's world people are constantly creating and sharing images. By manipulating pixels in PNGs, Stego allows the user to hide sensitive data *in plain sight*. 


The way this pixel manipulation is done (the "encoding method" or EM) is Stego's main focus, because the EM directly impacts whether the use of Stego will be detected. The first version of the EM simply replaced certain pixels' red bytes with the secret message's ASCII chars. But this method caused ASCII pixels to be differently colored than their neighboring pixels, and thus limited the number of ASCII chars that could be encoded per image before it became too obvious.


Upon the realization that pixels close together in everyday photos are colored similarly, Stego's current EM was made. The new method assigns a 2 pixel x 8 pixel tile from the image to each ASCII char. First the title's top row is colored identically to the bottom row. Then 0 or 1 is added to each of the 8 red bytes in the top row based on the binary representation of the ASCII char. 

![tile_definition](tile_definition.png)

Each tile's columns differ by at most 1 in red space, a difference virtually invisible to the human eye.

### SPACING parameter
The main drawback of this method is that up to half of the original pixels in the image have been replaced, so the image seems lower resolution. This is where `SPACING` comes in: `SPACING` is a user-definable parameter in `stego.py`: an integer >= 1. It represents how spread out the (low-res) ASCII tiles are in the encoded image, and thus the maximum chars that can be encoded. `SPACING=1` corresponds to tiles being packed together as close as possible (most resolution loss, most number of chars can be encoded). A higher `SPACING` decreases resolution loss but also decreases the number of chars that can be encoded. The user is encouraged to fiddle with this parameter; default value is `5`. 


## Dependencies

- Matplotlib

- NumPy

- [PyPNG](https://github.com/drj11/pypng): provided in distribution as `png.py`

## Acknowledgments
- Sample images included in `pool/` are from [PEXELS](https://www.pexels.com/) under CC0 License.