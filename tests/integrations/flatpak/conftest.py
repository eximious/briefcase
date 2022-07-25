from unittest import mock

import pytest

from briefcase.integrations.flatpak import Flatpak


@pytest.fixture
def flatpak():
    return Flatpak(
        subprocess=mock.MagicMock(),
        os=mock.MagicMock(),
    )
