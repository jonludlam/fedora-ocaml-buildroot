%ifarch %{ocaml_native_compiler}
%global native_compiler 1
%else
%global native_compiler 0
%endif

%global debug_package %{nil}

Name:           ocaml-cudf
Version:        0.7
Release:        3%{?dist}
Summary:        Common Upgradeability Description Format (CUDF) library

License:        LGPLv3 with exceptions
URL:            http://www.mancoosi.org/cudf/
Source0:        https://gforge.inria.fr/frs/download.php/file/33593/cudf-0.7.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlp4-devel

%description 
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%description devel
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains the development stuff needed to use libCUDF in your OCaml
programs.


%prep
%setup -q -n cudf-%{version}

%build
make
%if %{native_compiler}
make opt
%endif


%check
make test

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make -e install
rm $RPM_BUILD_ROOT%{_libdir}/ocaml/cudf/*.o

%files
%doc README
%doc COPYING
%{_libdir}/ocaml/cudf
%if %{native_compiler}
%exclude %{_libdir}/ocaml/cudf/*.a
%exclude %{_libdir}/ocaml/cudf/*.cmxa
%exclude %{_libdir}/ocaml/cudf/*.cmx
%endif
%exclude %{_libdir}/ocaml/cudf/*.mli

%files devel
%if %{native_compiler}
%{_libdir}/ocaml/cudf/*.a
%{_libdir}/ocaml/cudf/*.cmx
%{_libdir}/ocaml/cudf/*.cmxa
%endif
%{_libdir}/ocaml/cudf/*.mli


%changelog 
* Tue Feb 24 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.7-3
- Add COPYING doc and fix missing isa macro from devel Requires

* Wed Jan 21 2015 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.7-2
- Remove .o files from package

* Mon Dec 15 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.7-1
- Update for Fedora, and new version

* Tue Dec 22 2009 Stefano Zacchiroli <zack@pps.jussieu.fr>
- use default rpm installation paths (in particular, /usr/lib64 on x86_64)

* Sat Dec 19 2009 Stefano Zacchiroli <zack@pps.jussieu.fr>
- various adjustments (deps, description, native code, ...)

* Fri Dec 18 2009 Jeff Johnson <jbj@rpm5.org>
- create.


