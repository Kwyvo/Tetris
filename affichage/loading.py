from random import randint
from module.fltk import *
import asyncio


async def loading(h,l):
    val = 0
    while val < 100:
        val = randint(
            (val + 1 if val + 1 < 100 else val),
            (val + randint(7, 15) if val + randint(7, 15) < 100 else 100),
        )

        texte(l * 0.90, h * 0.90, f"{val}%", tag="loading_percentage", taille=15, couleur="white",police="Arial Black") # Affichage du texte de chargement
        mise_a_jour()
        efface("loading_percentage") # Efface uniquement le texte de pourcentage pour mise à jour
        await asyncio.sleep(0.05)
    
    texte(l * 0.90, h * 0.90, f"{val}%", tag="loading_percentage", taille=15, couleur="white",police="Arial Black")
    texte(l * 0.35, h * 0.80, "Press <left click> to start", taille=20, couleur="white",police="Arial Black")
    mise_a_jour()
        
async def loading_main(h,l):

    rectangle(0,0,l,h,remplissage='#0B1424')
    t1 = asyncio.create_task(animation_gif(l*0.50,h*0.50,"image/tetrisgif.gif", intervalle=20))
    t2 = asyncio.create_task(loading(h,l))
    await asyncio.gather(t1,t2)   
    
    attend_clic_gauche()