class Button():
    # The constructor sets the button's properties, such as its position and font. 
    # It also creates a text object using the passed text and font, and stores it in the "text" property. 
    # If no image is passed, the text object is used as the image of the button. 
    # The "rect" and "text_rect" properties are set to create the rectangles around the button and the text, respectively.
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))


    # check for any requests(button hover)
    def update(self, window):
        if self.image is not None:
            window.blit(self.image, self.rect)
        window.blit(self.text, self.text_rect)

    #check for any requests(button clicked)
    #this code essentially waits for the mouse to hover over and click
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    #change the color if the button is hovered over
    def changeColor(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)