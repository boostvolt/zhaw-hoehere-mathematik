import numpy as np
import numpy.linalg as lin


def a_in_ldr_zerlegen(A):
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    R = np.triu(A) - D
    return L, D, R


def ldr_zu_b_jacobi(L, D, R):
    return -lin.inv(D).dot(L + R)


def ldr_zu_b_gauss_seidel(L, D, R):
    return -lin.inv(L + D).dot(R)


def spektral_radius(matrix, debug=False):
    eigenwerte = np.linalg.eigvals(matrix)
    eigenwerte_betrag = np.abs(eigenwerte)

    if debug:
        print(f"Eigenwerte: {eigenwerte}")
        print(f"Eigenwerte im Betrag: {eigenwerte_betrag}")
        print()

    return np.max(eigenwerte_betrag)


########################################################################################

# Matrix definieren
A = np.array([[1, 0, 0], [2, 3, 0], [0, 1, 2]])

<<<<<<< HEAD
print(f"Spektralradius: {spektral_radius(A, debug=True)}")

=======
print(f"Spektralradius: {spektral_radius(A, True)}")
>>>>>>> 08744ec (add back code which was removed by mistake)

# Wenn Konvergenz von Jacobi oder Gauss-Seidel untersucht werden soll anhand dem Spektralradius
# Matrix definieren
A = np.array([[3, 2, 1], [2, 3, 2], [1, 2, 3]])
L, D, R = a_in_ldr_zerlegen(A)

# Jacobi
B = ldr_zu_b_jacobi(
    L,
    D,
    R,
)

print(f"Spektralradius für Jacobi: {spektral_radius(B, debug=False)}")

# Gauss-Seidel
B = ldr_zu_b_gauss_seidel(
    L,
    D,
    R,
)

print(f"Spektralradius für Gauss-Seidel: {spektral_radius(B, debug=False)}")
