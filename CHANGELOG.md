# Changelog

## 1.3.0 (2026-07-19)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v1.2.0...v1.3.0)

### Features

* add support for the /markets endpoint ([74744c1](https://github.com/SportsGameOdds/sports-odds-api-python/commit/74744c1bb24019bc51750dceecec21a6d5a2887e))
* initial stlc build ([af83bed](https://github.com/SportsGameOdds/sports-odds-api-python/commit/af83bedf96e4ce36b6e29306aff5ebeed5b07d57))
* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([e381e0c](https://github.com/SportsGameOdds/sports-odds-api-python/commit/e381e0cf00592a7868a1e393722961a949f41e31))


### Bug Fixes

* correct type errors and invalid kwargs in examples ([ad1a5aa](https://github.com/SportsGameOdds/sports-odds-api-python/commit/ad1a5aa2e22b2d77d424b8c3480794b195b9cfdf))

## 1.2.0 (2026-07-08)

Full Changelog: [v1.1.2...v1.2.0](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v1.1.2...v1.2.0)

### Features

* **client:** add support for binary request streaming ([957fa57](https://github.com/SportsGameOdds/sports-odds-api-python/commit/957fa570a945d29c0ed701273cb2a66f91a5f13d))


### Bug Fixes

* compat with Python 3.14 ([26662eb](https://github.com/SportsGameOdds/sports-odds-api-python/commit/26662eb2755d04f9452e908e6ee849174316a4f8))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([267ab9e](https://github.com/SportsGameOdds/sports-odds-api-python/commit/267ab9efaadbd2c04eb32fadd8f005d8bcd88320))
* ensure streams are always closed ([34dbbf9](https://github.com/SportsGameOdds/sports-odds-api-python/commit/34dbbf965b51566303019205eeeaa6ace7c9f5c4))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([8413151](https://github.com/SportsGameOdds/sports-odds-api-python/commit/841315114cadef22bd81f38f1ce272b0f04a895d))
* use async_to_httpx_files in patch method ([405dcb3](https://github.com/SportsGameOdds/sports-odds-api-python/commit/405dcb36386bfe8b844efd818973adbc55503f75))


### Chores

* add Python 3.14 classifier and testing ([ad06650](https://github.com/SportsGameOdds/sports-odds-api-python/commit/ad0665097975028fa2ef21f25cfc3606df7b70ae))
* **ci:** upgrade `actions/github-script` ([8fcde8d](https://github.com/SportsGameOdds/sports-odds-api-python/commit/8fcde8d7ab5d17e94a20828740a41600075574a4))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([63445c8](https://github.com/SportsGameOdds/sports-odds-api-python/commit/63445c815f942bf20aedf332300f787ff6018203))
* **docs:** use environment variables for authentication in code snippets ([9105cb3](https://github.com/SportsGameOdds/sports-odds-api-python/commit/9105cb3f988178c2581c16045264eed8df341804))
* **internal:** add `--fix` argument to lint script ([65658fa](https://github.com/SportsGameOdds/sports-odds-api-python/commit/65658fa131a827154e4321a13447ad428e87fdcd))
* **internal:** add missing files argument to base client ([b0e9e21](https://github.com/SportsGameOdds/sports-odds-api-python/commit/b0e9e21710675b2b1759a304a56120f6782ad9eb))
* **internal:** codegen related update ([012d5a4](https://github.com/SportsGameOdds/sports-odds-api-python/commit/012d5a4efcdb0d36780f3290f0535c01b09983b3))
* **internal:** codegen related update ([1572c08](https://github.com/SportsGameOdds/sports-odds-api-python/commit/1572c085be3b65fced016096e4103a4059ee00c5))
* **internal:** codegen related update ([6ee8773](https://github.com/SportsGameOdds/sports-odds-api-python/commit/6ee87739301154622858917c2ed76304fd844ebe))
* **internal:** codegen related update ([0901387](https://github.com/SportsGameOdds/sports-odds-api-python/commit/0901387e0570bf8b37794574349a8aee843ff1b8))
* **internal:** codegen related update ([a542b8b](https://github.com/SportsGameOdds/sports-odds-api-python/commit/a542b8b9d546235db986383f2836d7b64da2e8db))
* **internal:** codegen related update ([3201bd4](https://github.com/SportsGameOdds/sports-odds-api-python/commit/3201bd401b0bc74aa00392a61dd4f0cb1b070f98))
* **internal:** update `actions/checkout` version ([ea3785a](https://github.com/SportsGameOdds/sports-odds-api-python/commit/ea3785a8f7e6c40c50f2900004ee4b5beaf0e203))
* **package:** drop Python 3.8 support ([1eca400](https://github.com/SportsGameOdds/sports-odds-api-python/commit/1eca400a2f168a8ae03ea3491e6b049dc0c3f367))
* speedup initial import ([a799a71](https://github.com/SportsGameOdds/sports-odds-api-python/commit/a799a7173689a11304ab74c948b5d841d79ca35b))
* update lockfile ([e6b26a9](https://github.com/SportsGameOdds/sports-odds-api-python/commit/e6b26a9d279f367799d60b3badc82c3555701246))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([55b46dc](https://github.com/SportsGameOdds/sports-odds-api-python/commit/55b46dc684c798525fef55f521ca0e4ece13ad85))

## 1.1.2 (2025-11-04)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v1.1.1...v1.1.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([eae1c70](https://github.com/SportsGameOdds/sports-odds-api-python/commit/eae1c7004180153ae9662fcd5852d8fbcf7eb651))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([794a30d](https://github.com/SportsGameOdds/sports-odds-api-python/commit/794a30de6f17440b1ab18842f224cb5682bc6370))

## 1.1.1 (2025-10-25)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v1.1.0...v1.1.1)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([4ad809b](https://github.com/SportsGameOdds/sports-odds-api-python/commit/4ad809bd6be303c294a24a6f31555be1ce9a5699))
* **internal:** detect missing future annotations with ruff ([c33e446](https://github.com/SportsGameOdds/sports-odds-api-python/commit/c33e446780bc457e93b9d5340230f86a09e08146))

## 1.1.0 (2025-10-08)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v1.0.0...v1.1.0)

### Features

* test ([08e9d02](https://github.com/SportsGameOdds/sports-odds-api-python/commit/08e9d0200c7449750082cb5f0ae229012d9f633b))

## 1.0.0 (2025-09-22)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/SportsGameOdds/sports-odds-api-python/compare/v0.0.1...v1.0.0)

### Chores

* configure new SDK language ([2b0a24a](https://github.com/SportsGameOdds/sports-odds-api-python/commit/2b0a24a4c2ab45ac111edf93e70a3adb8781074d))
* update SDK settings ([1d5c8cb](https://github.com/SportsGameOdds/sports-odds-api-python/commit/1d5c8cbed9cdcb6f3c34a4b58afb83b6ca746781))
* update SDK settings ([77a5692](https://github.com/SportsGameOdds/sports-odds-api-python/commit/77a56927b45e9a3a2567bd22d76d4092a9c0effa))
