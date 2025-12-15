"""
Generate experiment entries

Not actually all experiments,
rather just those listed in
[Dunne et al., 2025](https://doi.org/10.5194/gmd-18-6671-2025)
for the CMIP7 fast-track.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict


class ExperimentUniverse(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    drs_name: str
    description: str
    activity: str
    additional_allowed_model_components: list[str]
    branch_information: str | None = "dont_write"
    end_timestamp: datetime | None | str
    min_ensemble_size: int
    min_number_yrs_per_sim: float | None | str = "dont_write"
    parent_activity: str | None = "dont_write"
    parent_experiment: str | None = "dont_write"
    parent_mip_era: str | None = "dont_write"
    required_model_components: list[str]
    start_timestamp: datetime | None | str
    tier: int | str = "dont_write"

    def write_file(self, universe_root: Path) -> None:
        id = self.drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "experiment",
            "drs_name": self.drs_name,
            "description": self.description,
            "activity": self.activity,
            "additional_allowed_model_components": self.additional_allowed_model_components,
            "min_ensemble_size": self.min_ensemble_size,
            "required_model_components": self.required_model_components,
        }

        for attr in (
            "branch_information",
            "min_number_yrs_per_sim",
            "parent_activity",
            "parent_experiment",
            "parent_mip_era",
            "tier",
            "start_timestamp",
            "end_timestamp",
        ):
            val = getattr(self, attr)
            if val != "dont_write":
                content[attr] = val

        out_file = str(universe_root / "experiment" / f"{id}.json")
        write_file(out_file, content)


class ExperimentProject(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    id: str
    activity: str
    description: str = "dont_write"
    branch_information: str | None = "dont_write"
    start_timestamp: datetime | None | str = "dont_write"
    end_timestamp: datetime | None | str = "dont_write"
    min_number_yrs_per_sim: float | None | str = "dont_write"
    min_ensemble_size: int | str = "dont_write"
    parent_activity: str | None = "dont_write"
    parent_experiment: str | None = "dont_write"
    parent_mip_era: str | None = "dont_write"
    tier: int

    def write_file(self, project_root: Path) -> None:
        content = {
            "@context": "000_context.jsonld",
            "id": self.id,
            "type": "experiment",
            "tier": self.tier,
        }

        for attr in (
            "branch_information",
            "description",
            "start_timestamp",
            "end_timestamp",
            "min_number_yrs_per_sim",
            "min_ensemble_size",
            "parent_activity",
            "parent_experiment",
            "parent_mip_era",
        ):
            val = getattr(self, attr)
            if val != "dont_write":
                content[attr] = val

        out_file = str(project_root / "experiment" / f"{self.id}.json")
        write_file(out_file, content)


class ActivityProject(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    id: str
    experiments: list[str]
    urls: list[str]
    description: str = "dont_write"

    def write_file(self, project_root: Path) -> None:
        content = {
            "@context": "000_context.jsonld",
            "id": self.id,
            "type": "activity",
            "experiments": sorted(self.experiments),
            "urls": sorted(self.urls),
        }
        for attr in ("description",):
            val = getattr(self, attr)
            if val != "dont_write":
                content[attr] = val

        out_file = str(project_root / "activity" / f"{self.id}.json")
        write_file(out_file, content)


class Holder(BaseModel):
    """
    God class :)
    """

    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
        strict=True,
    )

    experiments_project: list[ExperimentProject]
    experiments_universe: list[ExperimentUniverse]
    activities: list[ActivityProject]

    def initialise_activities(self) -> "Holder":
        self.activities = [
            ActivityProject(
                id="aerchemmip",
                experiments=[],
                urls=[
                    "https://doi.org/10.5194/gmd-10-585-2017",
                ],
            ),
            ActivityProject(
                id="c4mip",
                experiments=[],
                urls=[
                    "https://doi.org/10.5194/gmd-17-8141-2024",
                    "https://doi.org/10.5194/egusphere-2024-3356",
                    "https://doi.org/10.5194/gmd-9-2853-2016",
                ],
            ),
            ActivityProject(
                id="cfmip",
                experiments=[],
                urls=["https://doi.org/10.5194/gmd-10-359-2017"],
            ),
            ActivityProject(
                id="cmip",
                experiments=[],
                urls=["https://doi.org/10.5194/gmd-18-6671-2025"],
                description=(
                    # If you were doing this for CMIP6, you would write DECK and historical
                    # as historical was separate from the DECK in CMIP6, but isn't in CMIP7,
                    # see https://github.com/WCRP-CMIP/CMIP7-CVs/issues/327
                    "CMIP core common experiments "
                    "i.e. the DECK (Diagnostic, Evaluation and Characterization of Klima)."
                ),
            ),
            ActivityProject(
                id="damip",
                experiments=[],
                urls=["https://doi.org/10.5194/gmd-18-4399-2025"],
            ),
            ActivityProject(
                id="geomip",
                experiments=[],
                urls=[
                    "https://doi.org/10.5194/gmd-17-2583-2024",
                    "https://doi.org/10.1175/BAMS-D-25-0191.1",
                ],
            ),
            ActivityProject(
                id="pmip",
                experiments=[],
                urls=[
                    "https://doi.org/10.5194/gmd-10-3979-2017",
                    "https://doi.org/10.5194/cp-19-883-2023",
                ],
            ),
            ActivityProject(
                id="scenariomip",
                experiments=[],
                urls=["https://doi.org/10.5194/egusphere-2024-3765"],
                description=(
                    "Future scenario experiments. "
                    "Exploration of the future climate under a (selected) range of possible boundary conditions. "
                    "In CMIP7, the priority tier for experiments is conditional on whether you are doing emissions- or concentration-driven simulations. "
                    "There is no way to express this in the CVs (nor time to implement something to handle this conditionality). "
                    "This means that, for your particular situation, some experiments may be at a lower tier than is listed in the CVs. "
                    "For example, the `vl` scenario is tier 1 for concentration-driven models "
                    "and tier 2 for emissions-driven models. "
                    "However, in the CVs, we have used the highest priority tier (across all the possible conditionalities). "
                    "Hence `vl` is listed as tier 1 in the CVs (even though it is actually tier 2 for emissions-driven models)."
                    "For details, please see the full description in the ScenarioMIP description papers."
                ),
            ),
        ]

    def add_experiment_to_activity(self, experiment: ExperimentProject) -> "Holder":
        for activity_idx, activity in enumerate(self.activities):
            if activity.id == experiment.activity:
                break

        else:
            msg = f"No activity {experiment.activity} found. {self.activities=}"
            raise AssertionError(msg)

        if experiment.id not in self.activities[activity_idx]:
            self.activities[activity_idx].experiments.append(experiment.id)

        return self

    def add_1pctco2_entries(self) -> "Holder":
        for (
            drs_name,
            description_start,
            activity,
            required_model_components,
            additional_allowed_model_components,
        ) in (
            (
                "1pctCO2",
                "",
                "cmip",
                ["aogcm"],
                ["aer", "chem", "bgc"],
            ),
            (
                "1pctCO2-bgc",
                (
                    "Biogeochemically coupled simulation "
                    "(i.e. the carbon cycle only 'sees' the increase in atmospheric carbon dioxide, "
                    "not any change in temperature) of a "
                ),
                "c4mip",
                ["aogcm", "bgc"],
                ["aer", "chem"],
            ),
            (
                "1pctCO2-rad",
                (
                    "Radiatively coupled simulation "
                    "(i.e. the carbon cycle only 'sees' the increase in temperature, "
                    "not any change in atmospheric carbon dioxide) of a "
                ),
                "c4mip",
                ["aogcm", "bgc"],
                ["aer", "chem"],
            ),
        ):
            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=(
                    f"{description_start}"
                    "1% per year increase in atmospheric carbon dioxide levels. "
                    "All other conditions are kept the same as piControl."
                ),
                activity=activity,
                additional_allowed_model_components=additional_allowed_model_components,
                branch_information="Branch from `piControl` at a time of your choosing",
                end_timestamp=None,
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity="cmip",
                parent_experiment="picontrol",
                # Defined in project
                parent_mip_era="dont_write",
                required_model_components=required_model_components,
                start_timestamp=None,
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                min_number_yrs_per_sim=150,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_abruptco2_entries(self) -> "Holder":
        for drs_name, description_start, activity in (
            (
                "abrupt-4xCO2",
                "Abrupt quadrupling of atmospheric carbon dioxide levels.",
                "cmip",
            ),
            (
                "abrupt-2xCO2",
                "Abrupt doubling of atmospheric carbon dioxide levels.",
                "cfmip",
            ),
            (
                "abrupt-0p5xCO2",
                "Abrupt halving of atmospheric carbon dioxide levels.",
                "cfmip",
            ),
        ):
            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=(
                    f"{description_start} All other conditions are kept the same as piControl."
                ),
                activity=activity,
                additional_allowed_model_components=["aer", "chem", "bgc"],
                branch_information="Branch from `piControl` at a time of your choosing",
                end_timestamp=None,
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity="cmip",
                parent_experiment="picontrol",
                # Defined in project
                parent_mip_era="dont_write",
                required_model_components=["aogcm"],
                start_timestamp=None,
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                min_number_yrs_per_sim=300,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_amip_entries(self) -> "Holder":
        for (
            drs_name,
            description,
            activity,
            start_timestamp,
            end_timestamp,
            min_number_yrs_per_sim,
        ) in (
            (
                "amip",
                "Simulation of the climate of the recent past with prescribed sea surface temperatures and sea ice concentrations.",
                "cmip",
                "1979-01-01",
                "2021-12-31",
                43,
            ),
            (
                "amip-p4k",
                "Same as `amip` simulation, except sea surface temperatures are increased by 4K in ice-free regions.",
                "cfmip",
                "1979-01-01",
                "2021-12-31",
                43,
            ),
            (
                "amip-piForcing",
                (
                    "Same as `amip` simulation, except it starts in 1870 "
                    "and all forcings are set to pre-industrial levels "
                    "rather than time-varying forcings."
                ),
                "cfmip",
                "1870-01-01",
                "2021-12-31",
                152,
            ),
        ):
            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=description,
                activity=activity,
                additional_allowed_model_components=["aer", "chem", "bgc"],
                branch_information=None,
                end_timestamp=None,
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity=None,
                parent_experiment=None,
                parent_mip_era=None,
                required_model_components=["agcm"],
                start_timestamp=None,
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                start_timestamp=start_timestamp,
                end_timestamp=end_timestamp,
                min_number_yrs_per_sim=min_number_yrs_per_sim,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_picontrol_entries(self) -> "Holder":
        for (
            drs_name,
            description,
            min_number_yrs_per_sim,
            tier,
            parent_experiment,
            branch_information,
        ) in (
            (
                "piControl",
                (
                    "Pre-industrial control simulation "
                    "with prescribed carbon dioxide concentrations "
                    "(for prescribed carbon dioxide emissions, see `esm-piControl`). "
                    "Used to characterise natural variability and unforced behaviour."
                ),
                400,
                1,
                "picontrol-spinup",
                "Branch from `piControl-spinup` at a time of your choosing",
            ),
            (
                "piControl-spinup",
                (
                    "Spin-up simulation. "
                    "Used to get the model into a state of approximate radiative equilibrium "
                    "before starting the `piControl` simulation."
                ),
                None,
                3,
                None,
                None,
            ),
            (
                "esm-piControl",
                (
                    "Pre-industrial control simulation "
                    "with prescribed carbon dioxide emissions "
                    "(for prescribed carbon dioxide concentrations, see `piControl`). "
                    "Used to characterise natural variability and unforced behaviour."
                ),
                400,
                1,
                "esm-picontrol-spinup",
                "Branch from `esm-piControl-spinup` at a time of your choosing",
            ),
            (
                "esm-piControl-spinup",
                (
                    "Spin-up simulation. "
                    "Used to get the model into a state of approximate radiative equilibrium "
                    "before starting the `esm-piControl` simulation."
                ),
                None,
                3,
                None,
                None,
            ),
        ):
            if drs_name.startswith("esm-"):
                additional_allowed_model_components = ["aer", "chem"]
                required_model_components = ["aogcm", "bgc"]

            else:
                additional_allowed_model_components = ["aer", "chem", "bgc"]
                required_model_components = ["aogcm"]

            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=description,
                activity="cmip",
                additional_allowed_model_components=additional_allowed_model_components,
                branch_information=branch_information,
                end_timestamp=None,
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity=None if parent_experiment is None else "cmip",
                parent_experiment=parent_experiment,
                # Defined in project
                parent_mip_era=None if parent_experiment is None else "dont_write",
                required_model_components=required_model_components,
                start_timestamp=None,
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                min_number_yrs_per_sim=min_number_yrs_per_sim,
                parent_mip_era="cmip7" if parent_experiment is not None else None,
                tier=tier,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_historical_entries(self) -> "Holder":
        for (
            drs_name,
            description,
            parent_experiment,
            branch_information,
        ) in (
            (
                "historical",
                (
                    "Simulation of the climate of the recent past "
                    "(typically meaning 1850 to present-day) "
                    "with prescribed carbon dioxide concentrations "
                    "(for prescribed carbon dioxide emissions, see `esm-hist`)."
                ),
                "picontrol",
                "Branch from `piControl` at a time of your choosing",
            ),
            (
                "esm-hist",
                (
                    "Simulation of the climate of the recent past "
                    "(typically meaning 1850 to present-day) "
                    "with prescribed carbon dioxide emissions "
                    "(for prescribed carbon dioxide concentrations, see `historical`)."
                ),
                "esm-picontrol",
                "Branch from esm-piControl at a time of your choosing",
            ),
        ):
            if drs_name.startswith("esm-"):
                additional_allowed_model_components = ["aer", "chem"]
                required_model_components = ["aogcm", "bgc"]

            else:
                additional_allowed_model_components = ["aer", "chem", "bgc"]
                required_model_components = ["aogcm"]

            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=description,
                activity="cmip",
                additional_allowed_model_components=additional_allowed_model_components,
                branch_information=branch_information,
                # Defined in project
                end_timestamp="dont_write",
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity="cmip",
                parent_experiment=parent_experiment,
                # Defined in project
                parent_mip_era="dont_write",
                required_model_components=required_model_components,
                start_timestamp="1850-01-01",
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                start_timestamp="1850-01-01",
                end_timestamp="2021-12-31",
                min_number_yrs_per_sim=172,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_flat10_entries(self) -> "Holder":
        univ_flat10 = ExperimentUniverse(
            drs_name="esm-flat10",
            description="10 PgC / yr constant carbon dioxide emissions.",
            activity="c4mip",
            additional_allowed_model_components=["aer", "chem"],
            branch_information="Branch from `esm-piControl` at a time of your choosing",
            end_timestamp=None,
            min_ensemble_size=1,
            min_number_yrs_per_sim=100.0,
            parent_activity="cmip",
            parent_experiment="esm-picontrol",
            # Defined in project
            parent_mip_era="dont_write",
            required_model_components=["aogcm", "bgc"],
            start_timestamp=None,
            tier=1,
        )

        self.experiments_universe.append(univ_flat10)

        proj_flat10 = ExperimentProject(
            id=univ_flat10.drs_name.lower(),
            activity=univ_flat10.activity,
            parent_mip_era="cmip7",
            tier=1,
        )
        self.experiments_project.append(proj_flat10)
        self.add_experiment_to_activity(proj_flat10)

        for (
            drs_name,
            description,
            branch_information,
            min_number_yrs_per_sim,
        ) in (
            (
                "esm-flat10-cdr",
                (
                    "Extension of `esm-flat10` where emissions decline linearly to -10 PgC / yr "
                    "then stay constant until cumulative emissions "
                    "(including the emissions in `esm-flat10`) reach zero. "
                    "An extra 20 years is included at the end to allow for calculating averages over different time windows."
                ),
                "Branch from `esm-flat10` at the end of year 100.",
                220.0,
            ),
            (
                "esm-flat10-zec",
                "Extension of `esm-flat10` with zero emissions.",
                "Branch from `esm-flat10` at the end of year 100.",
                100.0,
            ),
        ):
            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=description,
                activity=univ_flat10.activity,
                additional_allowed_model_components=univ_flat10.additional_allowed_model_components,
                branch_information=branch_information,
                end_timestamp=None,
                min_ensemble_size=1,
                min_number_yrs_per_sim=min_number_yrs_per_sim,
                parent_activity=univ_flat10.activity,
                parent_experiment=proj_flat10.id,
                # Defined in project
                parent_mip_era="dont_write",
                required_model_components=univ_flat10.required_model_components,
                start_timestamp=None,
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                activity=univ.activity,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_damip_entries(self) -> "Holder":
        for drs_name, forcing in (
            ("hist-aer", "aerosol"),
            ("hist-GHG", "aerosol"),
            ("hist-nat", "aerosol"),
        ):
            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=(
                    f"Response to historical {forcing} forcing "
                    "(often with extension using forcings from a scenario simulation specific to the CMIP phase). "
                    "All other conditions are kept the same as piControl."
                ),
                activity="damip",
                additional_allowed_model_components=["aer", "chem", "bgc"],
                branch_information="Branch from `piControl` at a time of your choosing",
                # Defined in project
                end_timestamp="dont_write",
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity="cmip",
                parent_experiment="picontrol",
                # Defined in project
                parent_mip_era="dont_write",
                required_model_components=["aogcm"],
                # Defined in project
                start_timestamp="1850-01-01",
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                description=(
                    f"Response to historical {forcing} forcing "
                    "(with extension using forcings from the `m` scenario simulation). "
                    "All other conditions are kept the same as piControl."
                ),
                activity=univ.activity,
                start_timestamp="1850-01-01",
                end_timestamp="2035-12-31",
                min_number_yrs_per_sim=186,
                min_ensemble_size=3,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)

        return self

    def add_pmip_entries(self) -> "Holder":
        drs_name = "abrupt-127k"
        description = (
            "Simulation to examine the response to orbital and greenhouse gas concentration changes "
            "associated with the last interglacial (127 000 years before present)."
        )

        univ = ExperimentUniverse(
            drs_name=drs_name,
            description=description,
            activity="pmip",
            additional_allowed_model_components=["aer", "chem", "bgc"],
            branch_information="Branch from `piControl` at a time of your choosing",
            end_timestamp=None,
            min_ensemble_size=1,
            min_number_yrs_per_sim=100.0,
            parent_activity="cmip",
            parent_experiment="picontrol",
            parent_mip_era="dont_write",
            required_model_components=["aogcm"],
            start_timestamp=None,
            tier=1,
        )

        self.experiments_universe.append(univ)

        proj = ExperimentProject(
            id=univ.drs_name.lower(),
            activity=univ.activity,
            min_number_yrs_per_sim=100.0,
            parent_mip_era="cmip7",
            tier=1,
        )
        self.experiments_project.append(proj)

        self.add_experiment_to_activity(proj)

        return self

    @staticmethod
    def get_scenario_tier(drs_name: str) -> int:
        # A bit stupid, because in practice everything ends up being tier 1,
        # but ok at least we have the logic clarified now
        # (and can explain why it says this in the CVs if anyone asks).
        if drs_name.startswith("esm-"):
            # All standard scenarios are tier 1 for emissions-driven models
            return 1

        if any(v in drs_name for v in ("-vl-", "-h-")):
            # vl and h are tier 1 for experiments and extensions
            return 1

        if drs_name.endswith("-ext"):
            # Extensions are tier 1 up to 2150.
            # We can't express tier 1 up to 2150 and tier 2 otherwise
            # (we do that instead with min_number_yrs_per_sim)
            # so everything is just tier 1.
            return 1

        # If we get here, we are looking at concentration-driven experiments
        return 1

    @staticmethod
    def get_scenario_project(
        scenario_universe: ExperimentUniverse,
    ) -> ExperimentProject:
        res = ExperimentProject(
            id=scenario_universe.drs_name.lower(),
            activity=scenario_universe.activity,
            start_timestamp=scenario_universe.start_timestamp,
            end_timestamp=scenario_universe.end_timestamp,
            min_number_yrs_per_sim=scenario_universe.min_number_yrs_per_sim,
            parent_mip_era="cmip7",
            tier=scenario_universe.tier,
        )

        return res

    def get_scenario_extension(
        self,
        scenario: ExperimentUniverse,
    ) -> ExperimentUniverse:
        res = scenario.model_copy()

        scenario_end_timestamp_dt = datetime.strptime(
            scenario.end_timestamp, "%Y-%m-%d"
        )

        extension_start_timestamp = f"{scenario_end_timestamp_dt.year + 1}-01-01"
        extension_end_timestamp = "2500-12-31"

        res.description = f"Extension of `{scenario.drs_name}` beyond {scenario_end_timestamp_dt.year}."
        # Unclear to me how this is meant to work.
        # scenario ends at 2100-12-31, extensions starts at 2101-01-01.
        # Is it an implied join rather than a true overlap
        # (like we have for piControl to historical)?
        res.branch_information = f"Branch from `{scenario.drs_name}` at {scenario_end_timestamp_dt.strftime('%Y-%m-%d')}"

        res.start_timestamp = extension_start_timestamp
        res.end_timestamp = extension_end_timestamp

        res.min_number_yrs_per_sim = 50.0
        res.parent_activity = scenario.activity
        res.parent_experiment = scenario.drs_name.lower()
        res.drs_name = f"{scenario.drs_name}-ext"
        res.tier = self.get_scenario_tier(res.drs_name)

        return res

    @staticmethod
    def get_scenario_drs_name(scenario_acronym: str) -> str:
        return f"scen7-{scenario_acronym}"

    @staticmethod
    def get_scenario_esm_drs_name(scenario_drs_name: str) -> str:
        return f"esm-{scenario_drs_name}"

    def get_scenario_esm(
        self,
        scenario: ExperimentUniverse,
    ) -> ExperimentUniverse:
        res = scenario.model_copy()

        res.drs_name = self.get_scenario_esm_drs_name(scenario.drs_name)
        res.description = (
            scenario.description.replace(
                "carbon dioxide concentrations", "carbon dioxide emissions"
            )
            .replace("carbon dioxide emissions,", "carbon dioxide concentrations,")
            .replace(res.drs_name, scenario.drs_name)
        )
        res.required_model_components = ["aogcm", "bgc"]
        res.additional_allowed_model_components = ["aer", "chem"]

        if scenario.parent_experiment != "historical":
            raise AssertionError

        res.parent_experiment = "esm-hist"
        res.branch_information = scenario.branch_information.replace(
            scenario.parent_experiment, res.parent_experiment
        )

        res.tier = self.get_scenario_tier(res.drs_name)

        return res

    def add_scenario_entries(self) -> "Holder":
        acronym_descriptions = [
            ("vl", "PLACEHOLDER TBC. CMIP7 ScenarioMIP very low emissions future."),
            (
                "ln",
                "PLACEHOLDER TBC. CMIP7 ScenarioMIP low followed by negative (steep reductions begin in 2040, negative from TBD) emissions future.",
            ),
            ("l", "PLACEHOLDER TBC. CMIP7 ScenarioMIP low emissions future."),
            (
                "ml",
                "PLACEHOLDER TBC. CMIP7 ScenarioMIP medium followed by low (from 2040) emissions future.",
            ),
            ("m", "PLACEHOLDER TBC. CMIP7 ScenarioMIP medium emissions future."),
            (
                "hl",
                "PLACEHOLDER TBC. CMIP7 ScenarioMIP High followed by low (from 2060) emissions future.",
            ),
            ("h", "PLACEHOLDER TBC. CMIP7 ScenarioMIP high emissions future."),
        ]

        for acronym, description_base in acronym_descriptions:
            drs_name = self.get_scenario_drs_name(acronym)
            drs_name_esm_scenario = self.get_scenario_esm_drs_name(drs_name)
            if "CMIP7 ScenarioMIP" not in description_base:
                raise AssertionError(description_base)

            description = (
                f"{description_base} Run with prescribed carbon dioxide concentrations "
                f"(for prescribed carbon dioxide emissions, see `{drs_name_esm_scenario}`)."
            )

            univ_base = ExperimentUniverse(
                drs_name=drs_name,
                description=description,
                activity="scenariomip",
                additional_allowed_model_components=["aer", "chem", "bgc"],
                branch_information="Branch from `historical` at 2022-01-01.",
                end_timestamp="2100-12-31",
                min_ensemble_size=1,
                min_number_yrs_per_sim=79.0,
                parent_activity="cmip",
                parent_experiment="historical",
                parent_mip_era="cmip7",
                required_model_components=["aogcm"],
                start_timestamp="2022-01-01",
                tier=self.get_scenario_tier(drs_name),
            )

            proj_base = self.get_scenario_project(univ_base)

            self.experiments_universe.append(univ_base)
            self.experiments_project.append(proj_base)
            self.add_experiment_to_activity(proj_base)

            univ_ext = self.get_scenario_extension(univ_base)
            proj_ext = self.get_scenario_project(univ_ext)
            self.experiments_universe.append(univ_ext)
            self.experiments_project.append(proj_ext)
            self.add_experiment_to_activity(proj_ext)

            univ_esm = self.get_scenario_esm(univ_base)
            proj_esm = self.get_scenario_project(univ_esm)
            self.experiments_universe.append(univ_esm)
            self.experiments_project.append(proj_esm)
            self.add_experiment_to_activity(proj_esm)

            univ_esm_ext = self.get_scenario_extension(univ_esm)
            proj_esm_ext = self.get_scenario_project(univ_esm_ext)
            self.experiments_universe.append(univ_esm_ext)
            self.experiments_project.append(proj_esm_ext)
            self.add_experiment_to_activity(proj_esm_ext)

        return self

    def add_scenario_aerchemmip_entries(self) -> "Holder":
        for base in ["vl", "h"]:
            conc_driven_drs_name = self.get_scenario_drs_name(base)
            for base_drs_name in [
                conc_driven_drs_name,
                self.get_scenario_esm_drs_name(conc_driven_drs_name),
            ]:
                base_experiment_universe_l = [
                    v for v in self.experiments_universe if v.drs_name == base_drs_name
                ]
                if len(base_experiment_universe_l) != 1:
                    raise AssertionError(base_drs_name)
                base_experiment_universe = base_experiment_universe_l[0]

                for (
                    suffix,
                    required_model_components,
                    additional_allowed_model_components,
                    desc_suffix,
                ) in (
                    (
                        "-AQ",
                        ["aogcm", "aer", "chem"],
                        ["bgc"],
                        (
                            "This is for models with interactive chemistry. "
                            "Models without interactive chemistry should run "
                            f"`{base_experiment_universe.drs_name}-Aer` instead."
                        ),
                    ),
                    (
                        "-Aer",
                        ["aogcm", "aer"],
                        ["bgc", "chem"],
                        (
                            "This is for models without interactive chemistry. "
                            "Models with interactive chemistry should run "
                            f"`{base_experiment_universe.drs_name}-Aq` instead."
                        ),
                    ),
                ):
                    aerchemmip_experiment_universe = (
                        base_experiment_universe.model_copy()
                    )
                    aerchemmip_experiment_universe.drs_name = (
                        f"{aerchemmip_experiment_universe.drs_name}{suffix}"
                    )
                    aerchemmip_experiment_universe.activity = "aerchemmip"

                    desc_base = aerchemmip_experiment_universe.description.split(
                        " Run with prescribed"
                    )[0]
                    aerchemmip_experiment_universe.description = (
                        f"{desc_base} "
                        "Altered to use high aerosol and tropospheric non-methane ozone precursor emissions. "
                        f"{desc_suffix}"
                    )

                    aerchemmip_experiment_universe.min_ensemble_size = 3
                    aerchemmip_experiment_universe.required_model_components = (
                        required_model_components
                    )
                    aerchemmip_experiment_universe.additional_allowed_model_components = additional_allowed_model_components

                    aerchemmip_experiment_project = self.get_scenario_project(
                        aerchemmip_experiment_universe
                    )
                    self.experiments_universe.append(aerchemmip_experiment_universe)
                    self.experiments_project.append(aerchemmip_experiment_project)
                    self.add_experiment_to_activity(aerchemmip_experiment_project)

        # TODO: ask someone to translate/write hist-piAQ for me.
        # Not sure what hist-piAQ is or how it is defined.

    def add_geomip_entries(self) -> "Holder":
        for (
            drs_name,
            description_univ,
            description_proj_to_format,
            base_scenario,
            start_year,
        ) in (
            (
                "G7-1p5K-SAI",
                (
                    "Stablisation of global-mean temperature at 1.5C "
                    "by increasing stratospheric sulfur forcing "
                    "to whatever level is required to achieve stable temperatures. "
                    "The simulation generally branches from a scenario simulation at some point in the future."
                ),
                (
                    "Stablisation of global-mean temperature at 1.5C "
                    "by increasing stratospheric sulfur forcing "
                    "to whatever level is required to achieve stable temperatures "
                    "after following the `{scenario}` scenario until 2035."
                ),
                "scen7-ml",
                2035,
            ),
        ):
            description_proj = description_proj_to_format.format(scenario=base_scenario)
            start_timestamp = f"{start_year}-01-01"
            for exp_proj in self.experiments_project:
                if exp_proj.id == base_scenario:
                    parent = exp_proj
                    break
            else:
                raise AssertionError(base_scenario)

            univ = ExperimentUniverse(
                drs_name=drs_name,
                description=description_univ,
                activity="geomip",
                additional_allowed_model_components=["aer", "chem", "bgc"],
                # Defined in project
                branch_information="dont_write",
                end_timestamp="dont_write",
                min_ensemble_size=1,
                # Defined in project
                min_number_yrs_per_sim="dont_write",
                parent_activity="dont_write",
                parent_experiment="dont_write",
                parent_mip_era="dont_write",
                required_model_components=["aogcm"],
                # Defined in project
                start_timestamp="dont_write",
                tier=1,
            )

            self.experiments_universe.append(univ)

            proj = ExperimentProject(
                id=univ.drs_name.lower(),
                description=description_proj,
                branch_information=f"Branch from the `{base_scenario}` simulation at the start of {start_year}.",
                activity=univ.activity,
                start_timestamp=start_timestamp,
                end_timestamp=None,
                min_number_yrs_per_sim=50,
                min_ensemble_size=1,
                parent_activity=parent.activity,
                parent_experiment=parent.id,
                parent_mip_era="cmip7",
                tier=1,
            )
            self.experiments_project.append(proj)

            self.add_experiment_to_activity(proj)


        return self

    def write_files(self, project_root: Path, universe_root: Path) -> None:
        for experiment_project in self.experiments_project:
            experiment_project.write_file(project_root)

        for experiment_universe in self.experiments_universe:
            experiment_universe.write_file(universe_root)

        for activity in self.activities:
            activity.write_file(project_root)


def sort_keys(
    content: dict[str, Any],
    header_keys: tuple[str, ...] = (
        "@context",
        "id",
        "type",
        "description",
        "drs_name",
        "start_timestamp",
        "end_timestamp",
        "min_number_yrs_per_sim",
    ),
) -> dict[str, Any]:
    res = {}
    for k in header_keys:
        if k in content:
            res[k] = content[k]

    for k in sorted(content):
        if k in header_keys:
            continue

        res[k] = content[k]

    return res


def write_file(out_file: str, content: dict[str, Any]) -> None:
    content_sorted = sort_keys(content)
    with open(out_file, "w") as fh:
        json.dump(content_sorted, fh, indent=4)
        fh.write("\n")

    print(f"Wrote {out_file}")


def main():
    REPO_ROOT = Path(__file__).parents[1]
    project_root = REPO_ROOT / ".." / "CMIP7-CVs"
    universe_root = REPO_ROOT

    holder = Holder(experiments_project=[], experiments_universe=[], activities=[])

    holder.initialise_activities()

    holder.add_1pctco2_entries()
    holder.add_abruptco2_entries()
    holder.add_amip_entries()
    holder.add_picontrol_entries()
    holder.add_historical_entries()
    holder.add_flat10_entries()
    holder.add_damip_entries()
    holder.add_pmip_entries()
    holder.add_scenario_entries()
    holder.add_scenario_aerchemmip_entries()
    holder.add_geomip_entries()

    holder.write_files(project_root=project_root, universe_root=universe_root)


if __name__ == "__main__":
    main()
