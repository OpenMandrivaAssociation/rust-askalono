# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate askalono

Name:           rust-%{crate}
Version:        0.4.2
Release:        2%{?dist}
Summary:        Library to detect the contents of license files

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            https://crates.io/crates/askalono
Source:         %{crates_source}
# Initial patched metadata
# - Bump rmp-serde to 0.14.0: https://github.com/amzn/askalono/pull/50
Patch0:         askalono-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to detect the contents of license files.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc NOTICE README.md
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+spdx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+spdx-devel %{_description}

This package contains library source intended for building other packages
which use "spdx" feature of "%{crate}" crate.

%files       -n %{name}+spdx-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 17:26:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Fri Dec 06 01:04:40 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 10:11:05 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-3
- Regenerate

* Thu Apr 11 14:40:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-2
- Run tests in infrastructure

* Thu Mar 28 09:11:54 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Initial package
