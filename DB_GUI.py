import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,800])
base_font = pygame.font.Font(None,25)

pygame.display.set_caption("Student Database")

ID_rect = pygame.Rect(200,300,140,32)
FNAME_rect = pygame.Rect(260,300,140,32)
SNAME_rect = pygame.Rect(320,300,140,32)
AGE_rect = pygame.Rect(380,300,140,32)


run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.MOUSEBUTTONDOWN:
					if ID_rect.collidepoint(event.pos):
						IDactive = True
					else:
						IDactive = False
					if ID_rect.collidepoint(event.pos):
						FNAMEactive = True
					else:
						FNAMEactive = False
					if ID_rect.collidepoint(event.pos):
						SNAMEactive = True
					else:
						SNAMEacive = False	
					if ID_rect.collidepoint(event.pos):
						AGEactive = True
					else:
						AGEactive = False

	if event.type == pygame.KEYDOWN:
			if active == True:
				if event.key == pygame.K_BACKSPACE:
					user_text = user_text[:-1]
				else:
					user_text += event.unicode

				if IDactive == True:
					ID = user_text
				elif FNAMEactive == True:
					FNAME = user_text
				elif SNAMEactive == True:
					SNAME = user_text
				elif AGEactive == True:
					AGE = user_text

screen.fill((255,255,255))

colour = "gray15"

pygame.draw.rect(screen,colour,ID_rect,2)
pygame.draw.rect(screen,colour,FNAME_rect,2)
pygame.draw.rect(screen,colour,SNAME_rect,2)
pygame.draw.rect(screen,colour,AGE_rect,2)

ID_surface = base_font.render(ID,True,colour)
FNAME_surface = base_font.render(FNAME,True,colour)
SNAME_surface = base_font.render(SNAME,True,colour)
AGE_surface = base_font.render(AGE,True,colour)

screen.blit(ID_surface,ID_rect)
screen.blit(FNAME_surface,FNAME_rect)
screen.blit(SNAME_surface,SNAME_rect)
screen.blit(AGE_surface,AGE_rect)



pygame.display.flip()
clock.tick(60)
				
				

