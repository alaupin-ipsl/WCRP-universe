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

    def write_file(self, project_root: Path) -> None:
        content = {
            "@context": "000_context.jsonld",
            "id": self.id,
            "type": "activity",
            "experiments": sorted(self.experiments),
            "urls": sorted(self.urls),
        }

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

    holder.write_files(project_root=project_root, universe_root=universe_root)


if __name__ == "__main__":
    main()
