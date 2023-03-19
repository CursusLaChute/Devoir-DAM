
import numpy as np
import matplotlib.pyplot as plt

# Constants of the problem whatever the engine
# Attention, on devra trouver ces valeurs en dessous pendant l'atelier de dimensionnement
tau = 2  # valeur taux compression [-]
D = 2  # valeur alesage [m]
C = 3  # valeur course [m]
L = 4  # valeur longueur bielle [m]
Q = 1650  # valeur chaleur emise par fuel par kg de melange admis@ [J/kg_inlet gas]
mpiston = 5  # valeur masse piston@ [kg]
mbielle = 6  # valeur masse bielle  [kg]
gamma = 1.3  # Coeficient isentropique

# Some calculate constants
R = C/2
beta = L/R  # beta = L/R
theta = np.linspace(-2*np.pi, 2*np.pi, 1000)
thetaD = 0
deltaD = 0
Vc = np.pi * D**2 * R/2


def DV(theta): # Logiquement cette fonction est correcte
    return Vc/2 * (np.sin(theta) + np.sin(theta)*np.cos(theta)/np.sqrt(beta**2 - np.sin(theta)**2))


def Qtot(Q):
    pass


def DQ(theta, thetaD, deltaD, Qtot):
    pass


def plotPressure(x, fx):
    """
    :param x: Valeur des angles de vilebrequin
    :param fx: Les valeurs de l'evolution de la pression
    This function return nothing
    """
    plt.figure(figsize=(14, 7))
    plt.plot(x, fx)
    plt.title("Evolution de la pression à l'intérieur du cylindre", fontsize=14)
    plt.xlabel("Angle du vilebrequin thêta[rad]", fontsize=14)
    plt.ylabel("La pression p(thêta)[Pa]", fontsize=14)
    plt.show()
    return


def F_piston(rpm, theta,D,R,m_piston,m_bielle):
    """
    :param rpm: Vitesse de rotation en RPM
    :param theta: Valeur de l'angle de rotation
    :param D: Valeur du diametre du piston
    :param R: Valeur du rayon de vilbrequin
    :param pressure: Valeur de la pression
    :param m_piston: Valeur de la masse du piston
    :param m_bielle: Valeur de la masse de la bielle
    la fonction retourne la valeure de la force max et min exercée sur la bielle 
    """
    vit_ang = rpm*(np.pi/30)
    F_tete = (((np.pi*D**2)/4)*DV(theta))-(m_piston*R*vit_ang**2*np.cos(theta))
    F_pied = -(((np.pi*D**2)/4)*DV(theta)) + ((m_piston+m_bielle)*R*vit_ang**2*np.cos(theta)) 
    F_pied_min=min(F_pied)
    F_pied_max=max(F_pied)
    F_tete_min=min(F_tete)
    F_tete_max=max(F_tete)
    F_max=max(F_pied_max,F_tete_max)
    F_min=min(F_pied_min,F_tete_min)
    return F_max,F_min



def myfunc(rpm, s, theta, thetaC, deltaThetaC):
    """ 
    dimBielle dimensionnement d'une bielle
    dimBielle(rpm, s, theta, thetaC, deltaThetaC) calcules les données thermodynamiques
    et les forces d'un système Piston-Bielle-Vilebrequin afin de dimensionner la section
    d'une bielle.

    INPUTS :
    rpm : vitesse angulaire du moteur [rotation per minute]
    s : surcharge du moteur [-]
    theta : angle auxquels renvoyer les données [°]
    thetaC : angle d'allumage [°]
    deltaThetaC : durée de la combustion (en angle) [°] 
    theta : angle auxquels renvoyer les données [°]
    (Les angles sont donnés entre 0 et 720°)

    OUTPUTS :
    t : section de la bielle [m]
    V(theta) : Volume de la chambre de combustion en fonction de theta [m3]
    Q(theta) : chaleur dégagée par la combustion en fonction de theta [J]
    F_pied(theta) : [N]
    F_tete(theta) : [N]
    F_inertie(theta) : [N]
    (une force est positive si dirigée vers le haut).
    """

    V_output = 1 * np.ones_like(theta)
    Q_output = 2 * np.ones_like(theta)
    F_pied_output = 3 * np.ones_like(theta)
    F_tete_output = 4 * np.ones_like(theta)
    p_output = 5 * np.ones_like(theta)
    t = 6

    return V_output, Q_output, F_pied_output, F_tete_output, p_output, t


def main():
    # Gasoline engine
    Q = 1600
    print(Q)

    # Diesel engine
    Q = 2800
    print(Q)

    fx = DV(theta)
    plotPressure(theta, fx)

    F=F_piston()

    return


main()