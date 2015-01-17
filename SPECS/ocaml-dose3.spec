%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           ocaml-dose3
Version:        3.3
Release:        1%{?dist}
Summary:        Dose3 is a framework for managing distribution packages and their dependencies.
License:        LGPLv3 with exceptions
URL:            http://www.mancoosi.org/software/
Source0:        https://gforge.inria.fr/frs/download.php/file/34277/dose3-3.3.tar.gz
Patch0:         dose-fix-inst.patch
Patch1:         dose-rpm-buildfix.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-expat-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  zlib-devel
BuildRequires:  ocaml-curl-devel
BuildRequires:  rpm-devel


%description
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a
pool of libraries which enable analyzing packages coming from various
distributions.

Besides basic functionalities for querying and setting package
properties, dose3 also implements algorithms for solving more complex
problems (monitoring package evolutions, correct and complete
dependency resolution, repository-wide uninstallability checks).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        tools
Summary:        Tools for DOSE
 
%description    tools
Tools

%prep
%setup -q -n dose3-%{version}
%patch0
%patch1
%configure --with-zip --with-ocamlgraph --with-curl --with-xml --with-oUnit --with-rpm4

%build
make all

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$DESTDIR/%{_libdir}/ocaml
export BINDIR=$RPM_BUILD_ROOT/%{_bindir}
make -e install
cd doc/manpages
for man in *.?; do
    install -m644 $man -D %{buildroot}%{_mandir}/man1/$man
done
cd ../..


%files
%{_libdir}/ocaml/dose3
%if %{native_compiler}
%exclude %{_libdir}/ocaml/dose3/*.a
%exclude %{_libdir}/ocaml/dose3/*.cmxa
%endif
%exclude %{_libdir}/ocaml/dose3/*.mli

%files devel
%if %{native_compiler}
%{_libdir}/ocaml/dose3/*.a
%{_libdir}/ocaml/dose3/*.cmxa
%endif
%{_libdir}/ocaml/dose3/*.mli
%{_libdir}/ocaml/stublibs/dllrpm4_stubs.so
%{_libdir}/ocaml/stublibs/dllrpm4_stubs.so.owner

%files tools
%{_bindir}/apt-cudf
%{_bindir}/ceve
%{_bindir}/challenged
%{_bindir}/deb-buildcheck
%{_bindir}/deb-coinstall
%{_bindir}/debcheck
%{_bindir}/distcheck
%{_bindir}/eclipsecheck
%{_bindir}/outdated
%{_bindir}/rpmcheck
%{_bindir}/dominators-graph
%{_bindir}/smallworld
%{_bindir}/strong-deps
%{_mandir}/man1/apt-cudf.1.gz
%{_mandir}/man1/apt-cudf-get.8.gz
%{_mandir}/man1/apt-cudf.conf.5.gz
%{_mandir}/man1/ceve.1.gz
%{_mandir}/man1/buildcheck.1.gz
%{_mandir}/man1/distcheck.1.gz
%{_mandir}/man1/outdated.1.gz
%{_mandir}/man1/challenged.1.gz
%{_mandir}/man1/strongdeps.1.gz
%{_mandir}/man1/smallworld.1.gz
%{_mandir}/man1/debcoinstall.1.gz

%changelog
* Thu Dec 11 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-2
- Fix debuginfo package

* Wed Dec 10 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-1
- Update to 0.9.6

* Thu Jul 17 2014 David Scott <dave.scott@citrix.com> - 0.9.5-1
- Update to 0.9.5

* Fri May 30 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-3
- Split files correctly between base and devel packages

* Mon May 19 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub mirror

* Thu May 30 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

