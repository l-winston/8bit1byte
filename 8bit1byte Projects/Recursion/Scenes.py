from big_ol_pile_of_manim_imports import *

from math import cos, sin

class WhatIsRecursion(Scene):
    def construct(self):

        whatis = TexMobject(r"\text{What is }", r"\text{recursion}", r"\text{?}")
        whatis.set_color_by_tex("recursion", RED)
        whatis.scale(1.5)
        whatis.to_edge(UP)
        whatis.shift(2*DOWN)

        line1 = TexMobject(r"\text{Recursion}", r"\text{ is a }", r"\text{problem solving technique}", r"\text{ that involves }")
        line2 = TexMobject(r"\text{breaking a problem into }", r"\text{smaller}", r"\text{ and }", r"\text{easier}", r"\text{ to solve parts}")
        line1.set_color_by_tex("Recursion", RED)
        line1.set_color_by_tex("problem solving technique", YELLOW)
        line2.set_color_by_tex_to_color_map({
            "smaller" : BLUE,
            "easier" : BLUE
        })

        #     }", r"\text{

        whatisanswer = VGroup(line1, line2)
        whatisanswer.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        whatisanswer.next_to(whatis, 4*DOWN)

        self.play(FadeInFrom(whatis, direction=UP))
        self.wait(2)
        self.play(Write(whatisanswer), run_time=5)
        self.wait(2)

        whyuse = TexMobject(r"\text{Why use }", r"\text{recursion}", r"\text{?}")
        whyuse.set_color_by_tex("recursion", RED)
        whyuse.scale(1.5)
        whyuse.move_to(whatis)

        self.play(Transform(whatis, whyuse), FadeOut(whatisanswer), run_time=2)

        line3 = TexMobject(r"\text{Recursive}", r"\text{ solutions are almost always }")
        line4 = TexMobject(r"\text{simpler}", r"\text{ and }", r"\text{easier}", r"\text{ to come up with}")
        line3.set_color_by_tex("Recursive", RED)
        line4.set_color_by_tex_to_color_map({
            "simpler" : YELLOW,
            "easier" : BLUE
        })

        whyuseanswer = VGroup(line3, line4)
        whyuseanswer.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        whyuseanswer.next_to(whatis, 4*DOWN)

        self.play(Write(whyuseanswer), run_time=3)
        self.wait(2)

        whenuse = TexMobject(r"\text{When should you use }", r"\text{recursion}", r"\text{?}")
        whenuse.set_color_by_tex("recursion", RED)
        whenuse.scale(1.5)
        whenuse.move_to(whyuse)

        self.play(Transform(whatis, whenuse), FadeOut(whyuseanswer), run_time=2)

        line5 = TexMobject(r"\text{It's usually best to use }", r"\text{recursion}", r"\text{ when your problem }")
        line6 = TexMobject(r"\text{can be easily broken up into }", r"\text{smaller}", r"\text{ but }", r"\text{similar}", r"\text{ parts}")
        line5.set_color_by_tex("recursion", RED)
        line6.set_color_by_tex_to_color_map({
            "smaller" : YELLOW,
            "similar" : BLUE
        })

        whenuseanswer = VGroup(line5, line6)
        whenuseanswer.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        whenuseanswer.next_to(whatis, 4*DOWN)

        self.play(Write(whenuseanswer), run_time=3)
        self.wait(2)

        self.play(FadeOut(whatis), FadeOut(whenuseanswer), run_time=3)

class RecursionVSIteration(Scene):
    def construct(self):
        title = TexMobject(r"\text{Fibonacci Sequence}")
        title.scale(1.5)
        title.to_edge(UP)

        definefib = TexMobject(r"\text{A sequence where every number is the sum of the two numbers that precede it}")
        definefib.scale(0.8)
        sequence = TexMobject(r"\text{(Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)}")
        sequence.scale(0.7)
        fibintro = VGroup(definefib, sequence)
        fibintro.arrange_submobjects(DOWN, buff=SMALL_BUFF)
        fibintro.next_to(title, 2*DOWN)

        r = TexMobject(r"\text{Recursive}", r"\text{ Definition}")
        r.set_color_by_tex("Recursive", RED)
        r.move_to(ORIGIN)
        r.shift(4*LEFT+1*UP)
        i = TexMobject(r"\text{Iterative}", r"\text{ Definition}")
        i.set_color_by_tex("Iterative", BLUE)
        i.move_to(ORIGIN)
        i.shift(4*RIGHT+1*UP)

        rfibdef = TexMobject(r"a_{n}=a_{n-1}+a_{n-2}")
        rfibdef.move_to(ORIGIN)
        rfibdef.shift(LEFT*4)
        rfibdef.bg = SurroundingRectangle(rfibdef, color=YELLOW, fill_opacity=0)

        ifibdef = TexMobject(r"a_{n} = \frac{\phi^{n} - (-\phi)^{-n}}{\sqrt{5}}")
        phidef = TexMobject(r"\phi = 1.618033988749895...")

        fullidef = VGroup(ifibdef, phidef)
        fullidef.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        fullidef.move_to(ORIGIN)
        fullidef.shift(RIGHT*4)
        fullidef.bg = SurroundingRectangle(fullidef, color=YELLOW, fill_opacity=0)

        self.play(FadeInFrom(title, direction=UP))
        self.wait(2)
        self.play(Write(fibintro))
        self.wait(2)

        self.play(Write(r), Write(i))

        self.play(FadeOut(fibintro), ApplyMethod(r.shift, UP), ApplyMethod(i.shift, UP))

        self.play(Write(rfibdef), Write(fullidef))
        self.play(ShowCreation(rfibdef.bg), ShowCreation(fullidef.bg))

        self.wait(2)

class LinearSearch(Scene):
    def construct(self):
        title = TexMobject(r"\text{Linear Search}")
        title.scale(1.5)
        title.to_edge(UP)

        goal = TexMobject(r"\text{Goal: Find where the }", r"\text{circle}", r"\text{ is hidden}")
        goal.set_color_by_tex("circle", RED)
        goal.scale(0.6)
        goal.next_to(title, DOWN)

        line1 = TexMobject(r"\text{We can break up the array into two parts:}")
        line2 = TexMobject(r"\text{array[0]}", r"\text{ and }", r"\text{array}[1\overset{to}{\rightarrow}n]")
        line2.set_color_by_tex_to_color_map({
            r"\text{array[0]}" : BLUE,
            r"\text{array}[1\overset{to}{\rightarrow}n]" : PURPLE
        })

        explanation = VGroup(line1, line2)
        explanation.arrange_submobjects(DOWN, buff=SMALL_BUFF)
        explanation.next_to(goal, 2*DOWN)

        line3 = TexMobject(r"\text{We can easily check }", r"\text{array[0]}")
        line3.set_color_by_tex(r"\text{array[0]}", BLUE)
        line4 = TexMobject(r"\text{and checking }", r"\text{array}[1\overset{to}{\rightarrow}n]", r"\text{ is just a}")
        line4.set_color_by_tex(r"\text{array}[1\overset{to}{\rightarrow}n]", PURPLE)
        line5 = TexMobject(r"\text{smaller version of the original problem}")

        explanation2 = VGroup(line3, line4, line5)
        explanation2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        explanation2.next_to(goal, 2*DOWN)

        specialrect = Rectangle(fill_opacity=1, color=GOLD_A, height=1, width=1)
        circleind = 6
        squares = [Rectangle(fill_opacity=1, color=GOLD_A, height=1, width=1) if i != circleind else VGroup(Circle(fill_opacity=1,color=RED, radius=0.4), specialrect) for i in range(10)]

        for i in range(1, len(squares)):
            squares[i].next_to(squares[i-1], RIGHT/2)

        list = VGroup(*squares)
        list.move_to(ORIGIN+3*DOWN)

        self.play(FadeInFrom(title, direction=UP))
        self.play(ShowCreation(list), Write(goal))
        self.play(Write(explanation))
        self.wait(2)
        self.play(Transform(explanation, explanation2))

        for i in range(circleind+1):
            t3 = TexMobject(r"\text{We can easily check }", r"\text{array[" + str(i) + r"]}")
            t3.set_color_by_tex(r"\text{array[" + str(i) + r"]}", BLUE)
            t4 = TexMobject(r"\text{and checking }", r"\text{array}[" + str(i+1) + r"\overset{to}{\rightarrow}9]", r"\text{ is a smaller}")
            t4.set_color_by_tex(r"\text{array}[" + str(i+1) + r"\overset{to}{\rightarrow}9]", PURPLE)
            t5 = TexMobject(r"\text{version of the original problem}")

            temp = VGroup(t3, t4, t5)
            temp.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
            temp.next_to(goal, 2*DOWN)

            self.play(ApplyMethod(squares[i].shift, LEFT))
            arrow = Arrow(UP, DOWN).scale(0.75)
            arrow.next_to(squares[i], UP)
            if i != circleind:
                self.play(Transform(explanation, temp), GrowArrow(arrow), Transform(squares[i], Rectangle(fill_opacity=0, color=GOLD_A, height=1, width=1).move_to(squares[i])))
            else:
                self.play(Transform(explanation, temp), GrowArrow(arrow), Transform(specialrect, Rectangle(fill_opacity=0, color=GOLD_A, height=1, width=1).move_to(squares[i])))
                self.play(FadeOut(arrow))
                break

            self.play(Indicate(VGroup(*squares[i+1:])))
            self.play(FadeOut(arrow))

class BinarySearch(Scene):
    #     }", r"\text{

    def construct(self):
        title = TexMobject(r"\text{Binary Search}")
        title.scale(1.5)
        title.to_edge(UP)

        given = TexMobject(r"\text{Given: The array is }", r"\text{sorted}", r"\text{ in ascending order}")
        given.set_color_by_tex("sorted", YELLOW)
        given.scale(0.8)
        given.next_to(title, DOWN)

        goal = TexMobject(r"\text{Goal: Find where }", r"\text{11}", r"\text{ is}")
        goal.set_color_by_tex("11", RED)
        goal.scale(0.8)
        goal.next_to(title, DOWN)

        line1 = TexMobject(r"\text{We can break up the array into three parts:}")
        line2 = TexMobject(r"\text{array}[0\overset{to}{\rightarrow}n/2]", r"\text{, }", r"\text{array[n/2]}", r"\text{, and }", r"\text{array}[n/2+1\overset{to}{\rightarrow}n]")
        line2.set_color_by_tex_to_color_map({
            r"\text{array}[0\overset{to}{\rightarrow}n/2]" : BLUE,
            r"\text{array[n/2]}" : YELLOW,
            r"\text{array}[n/2+1\overset{to}{\rightarrow}n]" : PURPLE
        })

        explanation = VGroup(line1, line2)
        explanation.arrange_submobjects(DOWN, buff=SMALL_BUFF)
        explanation.next_to(goal, 2*DOWN)

        startbychecking = TexMobject(r"\text{Let's start by checking }", r"\text{array[n/2]}")
        startbychecking.set_color_by_tex(r"\text{array[n/2]}", BLUE)
        startbychecking.next_to(goal, 2*DOWN)

        line3 = TexMobject(r"\text{Since everything to the }", r"\text{left}", r"\text{ of }", r"\text{array[n/2]}", r"\text{ is smaller than }")
        line3.set_color_by_tex_to_color_map({
            r"\text{array[n/2]}" : BLUE,
            r"\text{left}" : YELLOW,
            r"\text{11}" : RED
        })

        line4 = TexMobject(r"\text{array[n/2]}", r"\text{, if }", r"\text{array[n/2]}", r" < ", r"\text{11}", r"\text{, we know }", r"\text{11}", r"\text{ can't be on its }", r"\text{left}")
        line4.set_color_by_tex_to_color_map({
            r"\text{array[n/2]}" : BLUE,
            r"\text{left}" : YELLOW,
            r"\text{11}" : RED
        })

        explanation2 = VGroup(line3, line4)
        explanation2.scale(0.8)
        explanation2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        explanation2.next_to(goal, 2*DOWN)

        line5 = TexMobject(r"\text{Since everything to the }", r"\text{right}", r"\text{ of }", r"\text{array[n/2]}", r"\text{ is greater than }")
        line5.set_color_by_tex_to_color_map({
            r"\text{array[n/2]}" : BLUE,
            r"\text{right}" : YELLOW,
            r"\text{11}" : RED
        })

        line6 = TexMobject(r"\text{array[n/2]}", r"\text{, if }", r"\text{array[n/2]}", r" > ", r"\text{11}", r"\text{, we know }", r"\text{11}", r"\text{ can't be on its }", r"\text{right}")
        line6.set_color_by_tex_to_color_map({
            r"\text{array[n/2]}" : BLUE,
            r"\text{right}" : YELLOW,
            r"\text{11}" : RED
        })

        explanation2reverse = VGroup(line5, line6)
        explanation2reverse.scale(0.8)
        explanation2reverse.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        explanation2reverse.next_to(goal, 2*DOWN)


        array = [1, 2, 7, 8, 11, 12, 14]
        squares = [Rectangle(fill_opacity=1, color=GOLD_A, height=1, width=1) for i in range(7)]
        nums = [TexMobject(str(array[i])) for i in range(7)]
        nums[4].set_color_by_tex("11", RED)

        for i in range(1, 7):
            squares[i].next_to(squares[i-1], RIGHT/2)
            nums[i].move_to(squares[i])

        sqandnums = [VGroup(nums[i], squares[i]) for i in range(7)]

        list = VGroup(*sqandnums)
        list.move_to(ORIGIN+3*DOWN)

        self.play(FadeInFrom(title, direction=UP))
        self.play(ShowCreation(list), Write(given))
        self.play(Transform(given, goal))
        self.play(Write(explanation))
        self.wait(2)
        self.play(Transform(explanation, startbychecking))
        self.play(Transform(explanation, explanation2))
        self.play(Transform(explanation, explanation2reverse))

        centers = [3, 1, 0]
        ranges = [(0, 7), (4, 7), (4, 5)]
        delete = [(0, 4), (1, 3), (0, 1)]
        keep = [(4, 7), (0, 1), (0, 0)]

        comparison = ["<", ">", "="]
        comparator = TexMobject("?").move_to(ORIGIN+DOWN)

        eleven = TexMobject("11").set_color_by_tex("11", RED).move_to(ORIGIN+RIGHT+DOWN)
        self.play(Write(comparator), Write(eleven))

        for i in range(len(centers)):
            arrow = Arrow(UP, DOWN).scale(0.5)
            arrow.next_to(squares[centers[i]], UP)
            self.play(Indicate(sqandnums[centers[i]]))
            self.play(GrowArrow(arrow), Transform(squares[centers[i]], Rectangle(fill_opacity=0, color=GOLD_A, height=1, width=1).move_to(squares[centers[i]])))
            self.play(ApplyMethod(nums[centers[i]].move_to, ORIGIN+LEFT+DOWN), FadeOut(arrow), Transform(comparator, TexMobject(comparison[i]).move_to(comparator)))
            self.play(FadeOut(VGroup(*sqandnums[delete[i][0]:delete[i][1]])))
            list = VGroup(*sqandnums[keep[i][0]:keep[i][1]])
            
            sqandnums = sqandnums[keep[i][0]:keep[i][1]]
            squares = squares[keep[i][0]:keep[i][1]]
            nums = nums[keep[i][0]:keep[i][1]]

            self.play(ApplyMethod(list.move_to, ORIGIN+3*DOWN))








        # for i in range(circleind+1):
        #     t3 = TexMobject(r"\text{We can easily check }", r"\text{array[" + str(i) + r"]}")
        #     t3.set_color_by_tex(r"\text{array[" + str(i) + r"]}", BLUE)
        #     t4 = TexMobject(r"\text{and checking }", r"\text{array}[" + str(i+1) + r"\overset{to}{\rightarrow}9]", r"\text{ is a smaller}")
        #     t4.set_color_by_tex(r"\text{array}[" + str(i+1) + r"\overset{to}{\rightarrow}9]", PURPLE)
        #     t5 = TexMobject(r"\text{version of the original problem}")
        #
        #     temp = VGroup(t3, t4, t5)
        #     temp.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        #     temp.next_to(goal, 2*DOWN)
        #
        #     self.play(ApplyMethod(squares[i].shift, LEFT))
        #     arrow = Arrow(UP, DOWN).scale(0.75)
        #     arrow.next_to(squares[i], UP)
        #     if i != circleind:
        #         self.play(Transform(explanation, temp), GrowArrow(arrow), Transform(squares[i], Rectangle(fill_opacity=0, color=GOLD_A, height=1, width=1).move_to(squares[i])))
        #     else:
        #         self.play(Transform(explanation, temp), GrowArrow(arrow), Transform(specialrect, Rectangle(fill_opacity=0, color=GOLD_A, height=1, width=1).move_to(squares[i])))
        #         self.play(FadeOut(arrow))
        #         break
        #
        #     self.play(Indicate(VGroup(*squares[i+1:])))
        #     self.play(FadeOut(arrow))
