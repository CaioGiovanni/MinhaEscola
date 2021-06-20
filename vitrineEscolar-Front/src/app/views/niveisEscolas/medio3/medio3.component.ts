import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-medio3',
  templateUrl: './medio3.component.html',
  styleUrls: ['./medio3.component.css']
})
export class EnsinoMedio3Component implements OnInit {

  constructor(private service:SharedService, private route: ActivatedRoute, private router:Router) { }

  EscolaList:any=[];

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
    });
  }

  detail(dataItem: any): void {
    this.router.navigate(['detail', dataItem.cep])
    this.service.selectedSchool = dataItem;
  }
}
