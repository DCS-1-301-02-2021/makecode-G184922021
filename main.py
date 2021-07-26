def on_hit(sprite: Sprite, othersprite: Sprite):
    othersprite.destroy(effects.fire, 100)
    info.change_score_by(1)

def on_a_pressed():
    global missile
    missile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 7 7 . . . . . . . . . . . . 
                    4 4 5 5 5 5 5 5 5 5 5 5 5 2 2 2 
                    . . 7 7 . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

bogy: Sprite = None
missile: Sprite = None
spacePlane: Sprite = None
scene.set_background_color(8)
spacePlane = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            9 9 9 9 9 . . . . . . . . . . . 
            9 1 1 9 9 . . . . . . . . . . . 
            . 1 1 . . . . . . . . . . . . . 
            . 1 1 1 1 1 . . . . . . . . . . 
            2 2 2 1 1 1 1 f 4 4 4 4 4 4 4 4 
            2 4 4 1 1 f f f 1 1 1 1 4 4 4 4 
            2 4 4 1 1 f 1 1 1 1 1 1 1 . . . 
            2 2 2 1 1 1 1 1 . . . . . . . . 
            . 1 1 1 1 1 1 . . . . . . . . . 
            . 1 1 1 . . . . . . . . . . . . 
            9 1 1 9 9 . . . . . . . . . . . 
            9 9 9 9 9 . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
info.set_life(3)
spacePlane.set_stay_in_screen(True)
controller.move_sprite(spacePlane, 200, 200)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_hit)
def on_on_overlap(sprite, othersprite):
    othersprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_update_interval():
    global bogy
    bogy = sprites.create(assets.image("""
        bogy
    """), SpriteKind.enemy)
    bogy.set_velocity(-100, randint(-30, 30))
    bogy.y = randint(0, scene.screen_height())
    bogy.left = scene.screen_width()
    bogy.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
