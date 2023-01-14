"""
Python Libraries - Manim

https://www.manim.community/
https://www.youtube.com/results?search_query=twoblue+one+brown
"""


from manim import *


class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        self.play(stream_lines.animate(run_time=10, lag_ratio=0.1).shift(UP * 2))
