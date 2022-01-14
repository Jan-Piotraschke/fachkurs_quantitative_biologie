using CairoMakie

struct ODE_Parameter{T}
    a::T
    b::T
end


p = ODE_Parameter(1.0,3.0)

# set the ODE problem
# odeSol(x,y) = Point(x*(1-x-y), y*(2-x-y)) # x'(t) = -x, y'(t) = 2y
odeSol(x,y) = Point(p.a-x*y, x*y-p.b*y) # x'(t) = -x, y'(t) = 2y

# define the figure visualization
fig = Figure(resolution = (700, 700), fontsize = 18, font = "sans")
# set up the axis
ax = Axis(fig, xlabel = "x", ylabel = "y", backgroundcolor = :white, axis=true)

# CALCULATION
x_axis = -4..4
y_axis = -4..4

# f and g are indepented of time t
f(x, y) = 1-x*y
g(x, y) = x*y-3*y  
# f(x, y) = x*(1-x-y)
# g(x, y) = y*(2-x-y)
myrange = -4:0.01:4

pltobj1 = contour!(myrange, myrange, f, levels=[0], color= "green")
pltobj2 = contour!(myrange, myrange, g, levels=[0], color= "red")

# https://makie.juliaplots.org/stable/examples/plotting_functions/streamplot/index.html 
# draw the tangent field
stplt = streamplot!(ax, odeSol, x_axis, y_axis, colormap = :magma, gridsize= (32,32), arrow_size = 5, linewidth = 0.5)
@info "the equation system is solved"

fig[1, 1] = ax
save("arrows_ex7.png", fig, px_per_unit = 2)



