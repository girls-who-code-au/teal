import pyglet
from pyglet import TileableTexture

FPS = 10 # frames per second (aka speed of the game)
WINDOW_BLOCK_WIDTH = 15 # number of blocks (aka size of the screen)
BLOCK_WIDTH = 50 # size of squares in pixels
FOOD_SCORE = 5 # points by food


window = pyglet.window.Window(fullscreen=True)
image = pyglet.resource.image('shaggy.jpg')
shaggy_tile = TileableTexture.create_for_image(image)

def draw_grid():
    """ Draw the grid lines of the board
    """
    pyglet.gl.glColor4f(0.23, 0.23, 0.23, 1.0)

    rows = columns = int(WINDOW_BLOCK_WIDTH)

    #Horizontal lines
    for i in range(rows):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, 
            ('v2i',(
			0,
			i * BLOCK_WIDTH,
			WINDOW_BLOCK_WIDTH * BLOCK_WIDTH,
			i * BLOCK_WIDTH)))
    #Vertical lines
    for j in range(columns):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,('v2i',(j * BLOCK_WIDTH, 0, j * BLOCK_WIDTH, WINDOW_BLOCK_WIDTH * BLOCK_WIDTH)))

@window.event
def on_draw():
	window.clear()
	#draw_grid()
	#image.blit(0,0)
	shaggy_tile.blit_tiled(0,0,0,8,8)

pyglet.app.run()
