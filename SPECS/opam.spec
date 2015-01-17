%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

Name:           opam
Version:        1.2.0~rc2
Release:        1%{?dist}
Summary:        OPAM package manager

License:        LGPLv3 with exceptions
URL:            http://opam.ocaml.org
Source0:        opam-1.2.0-rc2.tar.bz2

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlp4-devel

%description 
Opam

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
%description devel

%prep
%setup -q -n opam-1.2.0-rc2

%build
./configure --prefix /usr --libdir %{_libdir}
make


%check

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
export DESTDIR=$RPM_BUILD_ROOT
make -e install
make libinstall

%files
%{_bindir}/opam
%{_libdir}/ocaml/opam-lib
%if %{native_compiler}
%exclude %{_libdir}/ocaml/opam-lib/*.a
%exclude %{_libdir}/ocaml/opam-lib/*.cmxa
%exclude %{_libdir}/ocaml/opam-lib/*.cmx
%endif
%exclude %{_libdir}/ocaml/opam-lib/*.mli

%files devel
%if %{native_compiler}
%{_libdir}/ocaml/opam-lib/*.a
%{_libdir}/ocaml/opam-lib/*.cmx
%{_libdir}/ocaml/opam-lib/*.cmxa
%endif
%{_libdir}/ocaml/opam-lib/*.mli


%changelog 
* Wed Dec 17 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.2.0~rc2-1
- create.


