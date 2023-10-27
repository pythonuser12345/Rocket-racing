from Focus_Roots import*

rocket_x = 100
rocket_y = 300
rocket2_x = 400
rocket2_y = 300
saturn_y = 100
star_y = 150
star2_y = 250
star3_y = 200
star4_y = -1
star5_y = -150
star6_y = -70
circle_y = 600
win_y = 800
lose_y = 800

def change():
    global rocket_x,rocket_y,rocket2_x,rocket2_y,saturn_y,star_y,star2_y,star3_y,circle_y,star4_y,star5_y,star6_y,lose_y,win_y
    set_background(color_mid_night_blue)
    image("images/start-line.png",500,100,250,20)
    image("images/saturn.png",100,100,100,saturn_y)
    image("images/star.png",50,50,270,star_y)
    image("images/star.png",50,50,100,star2_y)
    image("images/star.png",50,50,450,star3_y)
    image("images/star.png",50,50,340,star4_y)
    image("images/star.png",50,50,400,star5_y)
    image("images/star.png",50,50,150,star6_y)
    draw_circle(250,circle_y,300,0,color=color_sea_green)
    image("images/rocket.png",200,200,rocket_x,rocket_y)
    image("images/rocket.png",200,200,rocket2_x,rocket2_y)
    image("images/winner.png",100,100,400,win_y)
    image("images/loser.png",100,100,100,lose_y)
    
    
    
    
    rocket_y = rocket_y-1
    rocket2_y = rocket2_y-2
    saturn_y = saturn_y+1
    star_y = star_y+1
    star2_y = star2_y+1
    star3_y = star3_y+1
    star4_y = star4_y+1
    star5_y = star5_y+1
    star6_y = star6_y+1
    circle_y = circle_y+1.5
    win_y = win_y-0.5
    lose_y = lose_y-0.5

    print(rocket_x,rocket_y) #100 rocket 1
    print(rocket2_x,rocket2_y) #400 rocket 2

draw(change)