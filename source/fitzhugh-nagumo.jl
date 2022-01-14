using CairoMakie

path = dirname(@__FILE__)
parent_dir = dirname(path)
path_img = joinpath(parent_dir, "img/fitzhugh_nagumo.png")

struct ODE_Parameter{T}
    a::T
end

# heavy-side function
function H(v,a)
    return v-a<0 ? 0 : 1
end

p = ODE_Parameter(0.5)

odeSol(v,w) = Point(- v - w + H(v,p.a), v) # x'(t) = -x, y'(t) = 2y

# define the figure visualization
fig = Figure(resolution = (700, 700), fontsize = 18, font = "sans")
# set up the axis
ax = Axis(fig, xlabel = "v", ylabel = "w", backgroundcolor = :white, axis=true, xticks=-2:0.5:2, yticks=[-0.5, 0.5])

# CALCULATION
x_axis = -3..3
y_axis = -3..3

# f and g are indepented of time t
f(v, w) = - v - w + H(v,p.a)
g(v, w) = v
myrange = -3:0.01:3

pltobj1 = contour!(myrange, myrange, f, levels=[0], color= "green")
pltobj2 = contour!(myrange, myrange, g, levels=[0], color= "red")

# https://makie.juliaplots.org/stable/examples/plotting_functions/streamplot/index.html 
# draw the tangent field
stplt = streamplot!(ax, odeSol, x_axis, y_axis, colormap = :magma, gridsize= (32,32), arrow_size = 5, linewidth = 0.5)
@info "the equation system is solved"

fig[1, 1] = ax
save(path_img, fig, px_per_unit = 2)