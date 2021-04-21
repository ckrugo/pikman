import graphics as gp


def test_graphics_version():
    """ Checks for the correct NumPy version as per specification """
    gp_ver = gp.__version__
    assert (gp_ver == "5.0")


def test_check_score():
    assert True
