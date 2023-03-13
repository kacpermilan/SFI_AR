from manim import *
    
class MixedReality(Scene):
    def construct(self):
        # Collide the Earth with Virtual World and create the Mixed Reality
        earth = ImageMobject("earth.png").move_to(ORIGIN + LEFT * 2.5)
        earthText = Text("Reality", color = BLUE).next_to(earth, DOWN)

        digitalCircle = Circle(1.1, color = PURPLE_A).move_to(ORIGIN + RIGHT * 2.5)
        digitalCircle.set_fill(YELLOW, opacity = 0.8)
        binaryCharacters = [Text(block, color = BLACK) for block in ["01100001", "01100010", "01100011"]]
        for i, block in enumerate(binaryCharacters):
            block.scale(0.6)
            block.move_to(digitalCircle.get_center())
            block.shift(UP * (i - 1) * 0.4)
        digitalWorld = VGroup(digitalCircle, *binaryCharacters)
        digitalText = Text("Digital World", color = YELLOW).next_to(digitalWorld, DOWN)

        mixedCircle = Circle(1.1, color = GREEN_D).move_to(ORIGIN)
        mixedCircle.set_fill([GREEN_D, BLUE_D], opacity = 0.8)
        mixedBinaryCharacters = [Text(block) for block in ["01100001", "01100010", "01100011"]]
        for i, block in enumerate(mixedBinaryCharacters):
            block.scale(0.6)
            block.move_to(mixedCircle.get_center())
            block.shift(UP * (i - 1) * 0.4)
        mixedReality = VGroup(mixedCircle, *mixedBinaryCharacters)
        mixedLabel = Text("Mixed Reality", color = GREEN_D).next_to(mixedReality, DOWN)

        # Animation part
        self.wait(1)
        self.play(FadeIn(earth))
        self.play(FadeIn(earthText))
        self.play(FadeIn(digitalWorld))
        self.play(FadeIn(digitalText))
        self.wait(2)
        self.play(earth.animate.move_to(ORIGIN), digitalWorld.animate.move_to(ORIGIN), FadeOut(earthText), FadeOut(digitalText))
        self.play(FadeIn(mixedReality), FadeOut(earth), FadeOut(digitalWorld))
        self.play(FadeIn(mixedLabel.next_to(mixedReality, DOWN)))
        self.wait(4)

        # Create scale
        scale = Line(start = LEFT * 5, end = RIGHT * 5)
        dividingLine = Line(start = ORIGIN, end = UP * 0.5)
        leftLine = Line(start = LEFT * 5, end = LEFT * 5 + UP * 0.5)
        leftLabel = Text("Augmented Reality", color = YELLOW).next_to(dividingLine, LEFT)
        rightLine = Line(start = RIGHT * 5, end = RIGHT * 5 + UP * 0.5)
        rightLabel = Text("Virtual Reality", color = PURPLE).next_to(dividingLine, RIGHT * 2.5)
        marks = VGroup(dividingLine, leftLine, rightLine)
        
        earth.next_to(leftLine, UP)
        digitalWorld.next_to(rightLine, UP * 2)

        # Animation part
        self.play(mixedReality.animate.move_to(ORIGIN + UP * 2))
        self.play(FadeIn(scale))
        self.play(Create(marks))
        self.play(FadeIn(earth))
        self.play(FadeIn(digitalWorld))
        self.play(mixedLabel.animate.next_to(scale, DOWN))
        self.play(leftLabel.animate.scale(0.5))
        self.play(rightLabel.animate.scale(0.5))
        self.play(*[obj.animate.shift(DOWN) for obj in self.mobjects])
        self.wait(4)