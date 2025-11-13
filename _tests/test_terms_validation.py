from wcrp_universe.models.consortium import Consortium
from wcrp_universe.models.forcing_index import ForcingIndex
from wcrp_universe.models.frequency import Frequency
from wcrp_universe.models.activity import Activity
from wcrp_universe.models.experiment import Experiment
from wcrp_universe.models.grid_label import GridLabel
from wcrp_universe.models.initialisation_index import InitialisationIndex
from wcrp_universe.models.institution import Institution
from wcrp_universe.models.license import License
from wcrp_universe.models.mip_era import MipEra
from wcrp_universe.models.model_component import ModelComponent
from wcrp_universe.models.organisation import Organisation
from wcrp_universe.models.physic_index import PhysicIndex
from wcrp_universe.models.product import Product
from wcrp_universe.models.realisation_index import RealisationIndex
from wcrp_universe.models.realm import Realm
from wcrp_universe.models.resolution import Resolution
from wcrp_universe.models.source import Source
from wcrp_universe.models.source_type import SourceType
from wcrp_universe.models.sub_experiment import SubExperiment
from wcrp_universe.models.table import Table
from wcrp_universe.models.date import Date
from wcrp_universe.models.time_range import TimeRange

from pathlib import Path
from wcrp_universe.models.variable import Variable
from wcrp_universe.models.variant_label import VariantLabel
from pydantic import ValidationError
import pytest


def validate_terms(input_dir, model):
    for p in input_dir.iterdir():
        if p.suffix==".json":
            try:
                # Load valid JSON into the model
               py_instance = model.model_validate_json(p.read_text())
            except ValidationError as exc:
                pytest.fail(f"ValidationError was raised for \nTerms : '{p.stem}'\nPath : {str(p)}\nError :  {exc.errors()[0]}")
 
def test_frequency():
    validate_terms(Path("frequency/"),Frequency)

def test_activity():
    validate_terms(Path("activity/"),Activity)

def test_experiment():
    validate_terms(Path("experiment/"),Experiment)

def test_sub_experiment():
    validate_terms(Path("sub_experiment/"),SubExperiment)


def test_source_type():
    validate_terms(Path("source_type/"),SourceType)

def test_source():
    validate_terms(Path("source/"),Source)

def test_license():
    validate_terms(Path("license/"),License)

def test_resolution():
    validate_terms(Path("resolution/"),Resolution)

def test_realm():
    validate_terms(Path("realm/"),Realm)

def test_model_component():
    validate_terms(Path("model_component/"),ModelComponent)

def test_institutions():
    validate_terms(Path("institution/"),Institution)

def test_consortias():
    validate_terms(Path("consortium/"),Consortium)

def test_organisation():
    validate_terms(Path("organisation/"),Organisation)

def test_grid():
    validate_terms(Path("grid/"),GridLabel)

def test_mip_era():
    validate_terms(Path("mip_era/"),MipEra)


def test_product():
    validate_terms(Path("product/"),Product)

def test_table():
    validate_terms(Path("table/"),Table)


def test_variable():
    validate_terms(Path("variable/"),Variable)


def test_realisation_index():
    validate_terms(Path("realisation_index/"),RealisationIndex)

def test_initialisation_index():
    validate_terms(Path("realisation_index/"),InitialisationIndex)

def test_physic_index():
    validate_terms(Path("realisation_index/"),PhysicIndex)

def test_forcing_index():
    validate_terms(Path("realisation_index/"),ForcingIndex)

def test_variant_label():
    validate_terms(Path("variant_label/"),VariantLabel)
def test_date():
    validate_terms(Path("date/"),Date)
def test_time_range():
    validate_terms(Path("time_range/"),TimeRange)
