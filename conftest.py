import pytest
from fixture.application import Application
from comtypes.client import CreateObject
import os


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\Education\\Python\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_xlsx(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_xlsx(file):
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.xlsx" % file)
    xl = CreateObject("Excel.Application")
    xl.Visible = True
    wb = xl.Workbooks.Open(filename)
    ws = wb.Sheets[1]
    data = []
    for row in range(1, 6):
        data.append(ws.Cells[row, 1].Value())
    xl.Quit()
    return data
