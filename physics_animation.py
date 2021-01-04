from manim import *

def custom_time(t,partitions,start,end,func):
	'''This function was taken from 
			Elteoremadebeethoven: https://github.com/Elteoremadebeethoven
		It is used to modify running time
	'''
	duration = end - start
	fragment_time = 1 / partitions
	start_time = start * fragment_time
	end_time = end * fragment_time
	duration_time = duration * fragment_time
	def fix_time(x):
		return (x - start_time) / duration_time
	if t < start_time: 
		return func(fix_time(start_time))
	elif start_time <= t < end_time:
		return func(fix_time(t))
	else:
		return func(fix_time(end_time))

def Custom(partitions,start,end,func=smooth):
	return lambda t: custom_time(t,partitions,start,end,func)


class Intro(Scene):

	def textsinfive(self, a, b, c, d, e):
	
		texts = (
			(Text(a), UP * 2.5),
			(Text(b), UP * 2 + RIGHT * 5),
			(Text(c), DOWN * 2 + RIGHT * 3),
			(Text(d), DOWN * 2 + LEFT * 3),
			(Text(e), UP * 2 + LEFT * 5)
			)

		T_5 = []
		for i in texts:
			T = i[0]
			T_5.append(i[0])
			T.scale(.7).move_to(i[1])
			self.play(Write(T))

		return VGroup(*T_5)

	def Physics(self):

		T = Text('Physics')
		T_latin = Text('physica')
		T_greek = Text('φυσικός')
		text_5 = (
			'Universe',
			'Energy', 
			'Matter',
			'Spacio-Time',
			'Fundamental\nInteractions'
			)
		self.play(Write(T))
		self.play(Transform(T, T_latin))
		self.play(Transform(T, T_greek))
		self.wait()
		self.play(Transform(T, Text('Physics')))
		self.wait()
		T_5 = self.textsinfive(*text_5)
		self.play(FadeOut(T_5))

	def ClassicalMechanics(self):

		T = Text("Classical mechanics").scale(.75).move_to(UP * 2.5)
		self.play(Write(T))
		self.wait()
		
		c = Circle().move_to(T).rotate(PI/2)
		p = Dot(color=RED).move_to(c, UP*1.5)
		MATX_force = MathTex(r'F = ma').move_to(p)

		self.play(Write(MATX_force))
		self.wait()
		self.play(Transform(MATX_force, p))
		self.play(MoveAlongPath(MATX_force, c))
		self.play(FadeOut(MATX_force))

	def Relativity(self):

		T = Text("Relativity").scale(.75).move_to(UP * 2 + RIGHT * 5)
		self.play(Write(T))
		self.wait()
		
		p = Dot(color=RED).next_to(T, DOWN + LEFT)
		MATX_energy = MathTex(r'E = mc^2').move_to(p)
		p_end = Dot(color=RED, radius = 0).next_to(T, DOWN + RIGHT)

		self.play(Write(MATX_energy))
		self.wait()
		self.play(Transform(MATX_energy, p))
		self.play(Transform(MATX_energy, p_end))
		self.play(FadeOut(MATX_energy))

	def Thermodynamics(self):
		T = Text("Thermodynamics").scale(.75).move_to(DOWN * 2 + RIGHT * 5)

		p = Dot().next_to(T, UP)

		p21 = Dot(color=GREEN).move_to(p)
		p22 = Dot(color=GREEN).next_to(p, LEFT)
		p23 = Dot(color=GREEN).next_to(p, RIGHT)


		p11 = Dot(color=RED).next_to(p22, LEFT)
		p12 = Dot(color=RED).next_to(p11, LEFT)
		p13 = Dot(color=RED).next_to(p12, LEFT)

		p31 = Dot(color=BLUE).next_to(p23, RIGHT)
		p32 = Dot(color=BLUE).next_to(p31, RIGHT)
		p33 = Dot(color=BLUE).next_to(p32, RIGHT)
		
		group = VGroup(
			p11, p12, p13,
			p21, p22, p23,
			p31, p32, p33)

		self.play(Write(T), FadeIn(group))
		
		for _ in range(4):
			self.play(
				ApplyMethod(p11.shift, 0.7*UP,
				 rate_func = Custom(10, 1, 10, func=there_and_back)), 
				ApplyMethod(p12.shift, 0.7*UP,
				 rate_func = Custom(10, 3, 10, func=there_and_back)), 
				ApplyMethod(p13.shift, 0.7*UP,
				 rate_func = Custom(10, 2, 10, func=there_and_back)), 

				ApplyMethod(p21.shift, 0.6*UP,
				 rate_func = Custom(10, 3, 8, func=there_and_back)), 
				ApplyMethod(p22.shift, 0.6*UP,
				 rate_func = Custom(10, 2, 8, func=there_and_back)), 
				ApplyMethod(p23.shift, 0.6*UP,
				 rate_func = Custom(10, 1, 8, func=there_and_back)), 

				ApplyMethod(p31.shift, 0.5*UP,
				 rate_func = Custom(10, 2, 6, func=there_and_back)), 
				ApplyMethod(p32.shift, 0.5*UP,
				 rate_func = Custom(10, 1, 6, func=there_and_back)), 
				ApplyMethod(p33.shift, 0.5*UP,
				 rate_func = Custom(10, 3, 6, func=there_and_back)))
		self.play(FadeOut(group))

	def Electromagnetism(self):

			T = Text("Electromagnetism").scale(.75).move_to(DOWN * 2.5)
			self.play(Write(T))

			svg = SVGMobject('images/electromagnetism.svg', stroke_width=0.75).scale(.5)
			svg.next_to(T, UP)
			self.play(
				Write(svg[:3]),
				FadeIn(svg[3:19].set_fill(opacity = 0).set_stroke(color=BLUE)),
				FadeIn(svg[19:].set_fill(opacity = 0).set_stroke(color=RED))
				)

			self.wait()
			self.play(FadeOut(svg))

	def Optics(self):
			T = Text("Optics").scale(.75).move_to(DOWN * 2 + LEFT * 5)
			self.play(Write(T))

			prism = Triangle()
			prism.next_to(T, UP)
			self.play(FadeIn(prism))

			center = prism.get_center()
			light_b = Line(center + .7*UP + LEFT, center)
			light_R = Line(center, center + .7*UP + 1.3*RIGHT, color=RED)
			light_O = Line(center, center + .7*UP + 1.2*RIGHT, color=ORANGE)
			light_Y = Line(center, center + .7*UP + 1.1*RIGHT, color=YELLOW)
			light_G = Line(center, center + .7*UP + RIGHT, color=GREEN)
			light_T = Line(center, center + .7*UP + 0.9*RIGHT, color=TEAL)
			light_B = Line(center, center + .7*UP + 0.8*RIGHT, color=BLUE)
			light_P = Line(center, center + .7*UP + 0.7*RIGHT, color=PURPLE)
			
			group = VGroup(
				prism,
				light_b,
				light_R,
				light_O,
				light_Y,
				light_G,
				light_T,
				light_B,
				light_P,
				)

			self.play(Write(light_b))
			self.play(
				Write(light_R), 
				Write(light_O),
				Write(light_Y), 
				Write(light_G),
				Write(light_T), 
				Write(light_B),
				Write(light_P),
				)

			self.play(FadeOut(group))

	def QuantumMechanics(self):
		T = Text('Quantum Mechanics').scale(.75).move_to(UP * 2 + LEFT * 4.5)
		self.play(Write(T))

		schrodinger =  r'i\hbar \frac{\partial}{\partial t}\Psi(r,t)= \hat{\mathcal{H}}\Psi(r,t)'
		p = Dot(color = RED).next_to(T, 1.6*UP)
		MATX_schrodinger = MathTex(schrodinger).scale(.75).move_to(p)
		sin_wave = SVGMobject('images/sin_wave.svg').set_fill(opacity=0).scale(0.5).move_to(p)

		self.play(FadeIn(sin_wave))
		self.play(Transform(sin_wave, MATX_schrodinger))
		self.wait()
		self.play(Transform(sin_wave, p))
		self.play(FadeOut(sin_wave))




	def construct(self):
		self.Physics()
		self.wait()  
		self.ClassicalMechanics() 
		self.wait() 
		self.Relativity() 
		self.wait() 
		self.Thermodynamics()
		self.wait()
		self.Electromagnetism()
		self.wait()
		self.Optics()
		self.wait()
		self.QuantumMechanics()
		self.wait()