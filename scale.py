from PIL import Image

class AdvMAME2x(object):
    """ A better implementation of Eric Johnston's aglorithm.
    """

    def __init__(self, img, scale):
        if img.mode != "RGB":
            self.img = img.convert("RGB")
        else:
            self.img = img
        self.scale = scale

    def is_power_of_two(self, num):
        """ Checks if given number is a number of two. Necessary because the
        algorithm cannot handle other scales.
        """

        return num & (num-1) and num > 0


    def __call__(self, scale):
        """ Can only scale images to powers of two
        """

        if (not isinstance(scale,int)) or (not is_power_of_two(scale)):
            raise TypeError("Scale for AdvMAME2x must be int and power of two")

        if scale > 2:
            # The algorithm works only for 2x scaling. To scale to
            # other powers of two, recursion is used.
            recurse = AdvMAME2x(self.img)
            recurse (scale/2)

        else :
            # TODO : actual algorithm here
            x,y = self.img.size
            original_data = self.img.load()

            target_x, target_y = (x*2, y*2)
            target_image = Image.new ("RGB", (target_x, target_y))
            target_data = target_image.load()

            # Algorithm does not work for pixels on the image border
            for i in range (1, target_x):
                for j in range (1, target_y):
                    target_data[2*i,2*j] = target_data[2*i+1,2*j] = target_data[2*i, 2*j] = target_data[2*i+1,2*j+1] = original_data[i,j]
                    if original_data[i-1,j]==original_data[i,j-1] and original_data[i-1,j]!=original_data[i+1,j] and original_data[i-1,j]!=original_data[i,j+1]:
                        target_data [2*i,2*j] = original_data[i-1,j]

                    if original_data[i-1,j]==original_data[i,j+1] and original_data[i-1,j]!=original_data[i+1,j] and original_data[i-1,j]!=original_data[i,j-1]:
                        target_data [2*i,2*j+1] = original_data[i-1,j]

                    if original_data[i+1,j]==original_data[i,j-1] and original_data[i-1,j]!=original_data[i+1,j] and original_data[i+1,j]!=original_data[i,j+1]:
                        target_data [2*i+1,2*j] = original_data[i+1,j]

                    if original_data[i+1,j]==original_data[i,j+1] and original_data[i-1,j]!=original_data[i+1,j] and original_data[i+1,j]!=original_data[i,j-1]:
                        target_data [2*i+1,2*j+1] = original_data[i+1,j]


class ImageScaler(object):
    """ Given an image and an algorithm, can be called to scale an image
    to specific resolution or scale.
    """

    def __init__(self, img, algorithm):
        """ Accepts target image and a scaling algorithm (implemented elsewhere)
	"""

        self.img = img
        self.algorithm = algorithm

    def __call__(self, target_resolution=None, scale=None):
        """ Expects target resolution or scale. If both are given scale is ignored.
        """

        if target_resolution is not None:
            # TODO
        elif scale is not None:
            # TODO
        else:
            raise TypeError ("Target resolution or scale epected")
