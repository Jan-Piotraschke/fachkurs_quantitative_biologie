using CairoMakie

struct ODE_Parameter{T}
    a::T
    b::T
    g::T
    d::T
end


p = ODE_Parameter(1.0, 3.0, 3.5, 1.0)

# set the ODE problem
# odeSol(x,y) = Point(x*(1-x-y), y*(2-x-y)) # x'(t) = -x, y'(t) = 2y
odeSol(x,y) = Point(p.a*x - p.b*x*y, p.g*x*y - p.d*y) # x'(t) = -x, y'(t) = 2y

# define the figure visualization
fig = Figure(resolution = (700, 700), fontsize = 18, font = "sans")
# set up the axis
ax = Axis(fig, xlabel = "x", ylabel = "y", backgroundcolor = :white, axis=true)

# CALCULATION
x_axis = 0..2.5
y_axis = 0..1.5

# https://makie.juliaplots.org/stable/examples/plotting_functions/streamplot/index.html 
# draw the tangent field
stplt = streamplot!(ax, odeSol, x_axis, y_axis, gridsize= (32,32), arrow_size = 5, linewidth = 0.5)
@info "the equation system is solved"

fig[1, 1] = ax
save("lotka_volterra.png", fig, px_per_unit = 2)



