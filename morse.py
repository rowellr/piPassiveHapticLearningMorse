import time

class Morse:

	def __init__(self, drv):
		self.drv = drv

	def play_letter(self, alphanum):
		self.play_sound(alphanum)
		getattr(self, 'morse_' + alphanum)()
		self.wait_letter()


	def play_string(self, letters):
		for letter in letters:
			if letter == ' ':
				self.wait_word()
			else:
				print letter
				self.play_letter(letter)


	def play_sound(self, alphanum):
		pass

	
    ##################################################
	# Dahs and Dits arrived at by trial and error
	# Feel free to find one that works for you!
	# see http://www.ti.com/lit/ds/symlink/drv2605.pdf for more info!
	##################################################

	def dah(self):
		self.drv.setWaveform(0, 14)
		self.drv.setWaveform(1, 0)  
		self.drv.go()
		time.sleep(0.32)
	
	def dit(self):
		self.drv.setWaveform(0, 1)
		self.drv.setWaveform(1, 0)  
		self.drv.go()
		time.sleep(0.18)

	def wait_letter(self):
		time.sleep(0.33)

	def wait_word(self):
		time.sleep(0.45)

	def morse_a(self):
		self.dit(); self.dah();
    

	def morse_b(self):
		self.dah(); self.dit(); self.dit(); self.dit();
    

	def morse_c(self):
		self.dah(); self.dit(); self.dah(); self.dit()
    

	def morse_d(self):
		self.dah(); self.dit(); self.dit();
    

	def morse_e(self):
		self.dit();
    

	def morse_f(self):
		self.dit(); self.dit(); self.dah(); self.dit();
    

	def morse_g(self):
		self.dah(); self.dah(); self.dit();
    

	def morse_h(self):
		self.dit(); self.dit(); self.dit(); self.dit();
    

	def morse_i(self):
		self.dit(); self.dit();

		
	def morse_j(self):
		self.dit(); self.dah(); self.dah(); self.dah();
    

	def morse_k(self):
		self.dah(); self.dit(); self.dah();
    
        
	def morse_l(self):
		self.dit(); self.dah(); self.dit(); self.dit();
    
        
	def morse_m(self):
		self.dah(); self.dah();
    
        
	def morse_n(self):
		self.dah(); self.dit();
    

	def morse_o(self):
		self.dah(); self.dah(); self.dah();
    

	def morse_p(self):
		self.dit(); self.dah(); self.dah(); self.dit();
    

	def morse_q(self):
		self.dah(); self.dah(); self.dit(); self.dah();
    

	def morse_r(self):
		self.dit(); self.dah(); self.dit();
    
        
	def morse_s(self):
		self.dit(); self.dit(); self.dit();
    
        
	def morse_t(self):
		self.dah();
    
        
	def morse_u(self):
		self.dit(); self.dit(); self.dah();
    
        
	def morse_v(self):
		self.dit(); self.dit(); self.dit(); self.dah();
    
        
	def morse_w(self):
		self.dit(); self.dah(); self.dah();
    
        
	def morse_x(self):
		self.dah(); self.dit(); self.dit(); self.dah();
    
        
	def morse_y(self):
		self.dah(); self.dit(); self.dah(); self.dah();
    
        
	def morse_z(self):
		self.dah(); self.dah(); self.dit(); self.dit();
    
        
	def morse_1(self):
		self.dit(); self.dah(); self.dah(); self.dah(); self.dah();
    
        
	def morse_2(self):
		self.dit(); self.dit(); self.dah(); self.dah(); self.dah();
    
        
	def morse_3(self):
		self.dit(); self.dit(); self.dit(); self.dah(); self.dah();
    
        
	def morse_4(self):
		self.dit(); self.dit(); self.dit(); self.dit(); self.dah();
    
        
	def morse_5(self):
		self.dit(); self.dit(); self.dit(); self.dit(); self.dit();
    
        
	def morse_6(self):
		self.dah(); self.dit(); self.dit(); self.dit(); self.dit();
    
        
	def morse_7(self):
		self.dah(); self.dah(); self.dit(); self.dit(); self.dit();
    
        
	def morse_8(self):
		self.dah(); self.dah(); self.dah(); self.dit(); self.dit();
    
                
	def morse_9(self):
		self.dah(); self.dah(); self.dah(); self.dah(); self.dit();
    
        
	def morse_0(self):
		self.dah(); self.dah(); self.dah(); self.dah(); self.dah();

