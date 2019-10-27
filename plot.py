from matplotlib import pyplot as plt
import numpy as np
import classnition
import dividingPlanes

fig = plt.figure()
ax = fig.add_subplot(111)
legend_map = {
    1: 'or',
    2: 'ob',
    3: 'og',
    4: 'om',
}


def build_plot(classes):
    global classes_array
    classes_array = classes

    k = 1
    p = []

    fig.suptitle('The study of geometric measures of proximity of \n objects and classes in recognition systems',
                 fontsize=10, fontweight='bold')

    fig.subplots_adjust(top=0.85)
    fig.canvas.mpl_connect('button_press_event', onclick)

    for class_array in classes:
        for j in enumerate(class_array):
            p1, = plt.plot(class_array[:, 0], class_array[:, 1], legend_map[k])
        p.append(p1)
        k += 1

    ax.legend(p, ["class1", "class2", "class3", "class4"])
    ax.grid(True)
    plt.show()


def onclick(event):
    ax.plot(event.xdata, event.ydata,
            legend_map[classnition.euklid_class_number(classes_array, np.array([event.xdata, event.ydata]))])
    plt.show()

