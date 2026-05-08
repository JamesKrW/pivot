import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai", "0007_alter_strategyrecommendation_rationale"),
    ]

    operations = [
        migrations.CreateModel(
            name="StrategyScenarioFrame",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "scenario_case",
                    models.CharField(choices=[("base", "Base"), ("bull", "Bull"), ("bear", "Bear")], max_length=10),
                ),
                ("direction", models.CharField(max_length=32)),
                ("catalysts", models.JSONField()),
                ("invalidating_conditions", models.JSONField()),
                (
                    "confidence_band",
                    models.CharField(choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], max_length=10),
                ),
                ("risk_notes", models.TextField()),
                ("position_size_guidance", models.TextField()),
                ("generated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "recommendation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scenario_frames",
                        to="ai.strategyrecommendation",
                    ),
                ),
            ],
            options={
                "db_table": "strategy_scenario_frames",
                "ordering": ["generated_at"],
            },
        ),
        migrations.AddIndex(
            model_name="strategyscenarioframe",
            index=models.Index(fields=["recommendation", "scenario_case"], name="strategy_sc_recomme_68964d_idx"),
        ),
        migrations.AddConstraint(
            model_name="strategyscenarioframe",
            constraint=models.UniqueConstraint(
                fields=("recommendation", "scenario_case"),
                name="unique_strategy_scenario_case_per_recommendation",
            ),
        ),
    ]
